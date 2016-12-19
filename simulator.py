import cloud, device, network, packet, data
from packet import Packet
import heapq

CLOUD = 0
MAX_PACKETS_PER_STEP = 350 # https://blog.cloudflare.com/how-to-receive-a-million-packets/

class Simulator(object):

	def __init__(self, cloud, network, devices, simTime):
		self.endpoints = [cloud] + devices
		self.network = network
		self.time = 0
		self.endTime = simTime

		# Priority queue of tuples (timestamp+elapsedtime, packet)
		self.activePackets = []

	def run(self):
		totalTimeStr = str(self.endTime)
		for timeStep in xrange(self.endTime):
			if timeStep % 100 == 0:
				print "\r" + "Computing time step: " + str(timeStep) + " out of " + totalTimeStr,
			self.runStep(timeStep)

	def getResults(self):
		results = []
		for deviceID in xrange(1, self.numEndpoints()):
			results.append(self.endpoints[deviceID].data)
		return results

	def numEndpoints(self):
		return len(self.endpoints)

	def runStep(self, step):
		self.deliverReadyPackets(step)
		self.updateActivePackets(step)

	def sendThruNetwork(self, packet):
		senderLocation = self.locationOf(packet.sender)
		receiverLocation = self.locationOf(packet.receiver)
		response = self.network.networkDelay(senderLocation, receiverLocation)
		if self.dropped(response):
			return None
		else:
			delay = response
			packet.addLatency(delay)
			return packet

	def dropped(self, response):
		return response is None

	def addActivePacket(self, packet):
		toAdd = (packet.arriveTime(), packet)
		heapq.heappush(self.activePackets, toAdd)

	def nextActivePacket(self):
		return self.activePackets[0][1]

	def hasActivePackets(self):
		return len(self.activePackets) > 0

	def popActivePacket(self):
		return heapq.heappop(self.activePackets)[1]

	def deliverReadyPackets(self, step):
		self.resetDeliveryCounts()
		if self.hasActivePackets() and self.nextActivePacket().isReady(step):
			self.deliverPacket(self.popActivePacket())

	def deliverPacket(self, packet):
		dest = packet.receiver
		if self.deliveryCounts[dest] <= MAX_PACKETS_PER_STEP:
			self.endpoints[dest].receivePacket(packet)
			self.incrementDeliveryCountFor(dest)

	def incrementDeliveryCountFor(self, deviceID):
		self.deliveryCounts[deviceID] += 1

	def updateActivePackets(self, step):
		for endpoint in self.endpoints:
			response = endpoint.responseAt(step)
			if response is not None:
				for packet in response:
					self.queuePacket(packet)

	def queuePacket(self, packet):
		networkResponse = self.sendThruNetwork(packet)
		if isinstance(networkResponse, Packet):
			self.addActivePacket(networkResponse)

	def resetDeliveryCounts(self):
		self.deliveryCounts = [0] * len(self.endpoints)

	def locationOf(self, deviceID):
		return self.endpoints[deviceID].location
