from packet import Packet,PacketQueue

# these delays can be seen as the time response time of the server for each game
# being played

MAX_PACKETS_PER_STEP = 350
TRAFFIC_DELAY = { 'high' : 10, 'med' : 5, 'low' : 3 }

class Cloud(object):

	def __init__(self, gameTraffic, location, timeout, num_players):
		self.timeToProcess = TRAFFIC_DELAY[gameTraffic]
		self.num_players = num_players
		self.location = location
		self.timeout = timeout
		self.requestList = PacketQueue()
		self.time = 0

	def step(self):
		self.time += 1
		responsePackets = []
		while not self.requestList.empty() \
				and self.requestList.next().isReady(self.time) \
				and len(responsePackets) <= MAX_PACKETS_PER_STEP:
			headPacket = self.requestList.pop()
			if headPacket.arriveTime() < self.time:
				headPacket.addLatency(self.time - headPacket.arriveTime())
			for i in xrange(1, self.num_players + 1):
				newPacket = headPacket.deepcopy()
				newPacket.sender = 0
				newPacket.receiver = i
				responsePackets.append(newPacket)
		return responsePackets

	def receivePacket(self, packet):
		packet.addLatency(self.timeToProcess)
		self.requestList.push(packet)
