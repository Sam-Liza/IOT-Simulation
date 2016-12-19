import cloud, device, network, packet, data
from packet import Packet,PacketQueue

CLOUD = 0
MAX_PACKETS_PER_STEP = 350 # https://blog.cloudflare.com/how-to-receive-a-million-packets/

class Simulator(object):

	def __init__(self, cloud, network, devices):
		self.endpoints = [cloud] + devices
		for i in xrange(self.numEndpoints()): self.endpoints[i].id = i
		self.network = network
		self.packetqueue = PacketQueue()
		self.time = 0

	def runFor(self, time):
		for t in xrange(self.time, self.time + time + 1):
			if t % 256 == 0 or t == time: _printProgress(t, self.time + time + 1)
			self.step()

	def getResults(self):
		return [self.endpoints[i].data for i in xrange(1, self.numEndpoints())]

	def step(self):
		self.time += 1

		deliveryCounts = [0] * self.numEndpoints()
		while not self.packetqueue.empty() \
				and self.packetqueue.next().isReady(self.time):
			packet = self.packetqueue.pop()
			dest = packet.receiver
			if deliveryCounts[dest] <= MAX_PACKETS_PER_STEP:
				self.endpoints[dest].receivePacket(packet)
				deliveryCounts[dest] += 1
			else:
				pass # Packet lost due to buffer overflow

		for endpoint in self.endpoints:
			response = endpoint.step()
			for packet in response:
				networkResponse = self.sendThruNetwork(packet)
				if networkResponse is not None:
					self.packetqueue.push(networkResponse)

	def sendThruNetwork(self, packet):
		senderLocation = self.locationOf(packet.sender)
		receiverLocation = self.locationOf(packet.receiver)
		response = self.network.networkDelay(senderLocation, receiverLocation)
		if response is None:
			return None
		else:
			delay = response
			packet.addLatency(delay)
			return packet

	def locationOf(self, deviceID):
		return self.endpoints[deviceID].location

	def numEndpoints(self):
		return len(self.endpoints)

def _printProgress(currstep, total):
	print "\rComputing time step: %d to %d" % (currstep, total),

