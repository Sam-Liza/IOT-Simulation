import Queue
if __name__ == "__main__": import packet

# these delays can be seen as the time response time of the server for each game
# being played

TRAFFIC_DELAY = { 'high' : 10, 'med' : 5, 'low' : 3 }

class Cloud(object):

	def __init__(self, gameTraffic, location, timeout, num_players):

		self.requestList = Queue.Queue()

		self.timeToProcess = TRAFFIC_DELAY[gameTraffic]

		self.num_players = num_players
		self.location = location
		self.timeout = timeout

	def responseAt(self, time):
		if time % self.timeToProcess == 0 and not self.requestList.empty() :
			headPacket = self.requestList.get();
			if (time - headPacket.timestamp) >  self.timeout:
				return None
			else:
				responsePackets = []
				for i in range(1,self.num_players):
					newPacket = headPacket

					# update packet
					newPacket.sender = 0
					newPacket.receiver = i

					responsePackets.append(newPacket)
				return responsePackets
		else:
			return None

	def receivePacket(self, packet):
		self.requestList.put(packet)


if __name__ == "__main__":
	packet1 = packet.Packet(100, 0, 0, 1)
	packet2 = packet.Packet( 0, 0, 0, 2)
	packet3 = packet.Packet(100, 0, 0, 1)
	packet4 = packet.Packet( 100, 0, 0, 2)

	cloud = cloud.Cloud(0, 0, 10, 10)

	cloud.receivePacket(packet1)
	cloud.receivePacket(packet4)
	cloud.receivePacket(packet3)
	cloud.receivePacket(packet2)

	time = 100
	print "\ntest 1: should return 3 packets"
	for i in range(0,20):
		#print time
		packetList = cloud.updateTime(time)
		if packetList != None:
			print packetList[0].packet_id
		time = time + 1

	cloud.receivePacket(packet1)
	cloud.receivePacket(packet2)
	cloud.receivePacket(packet3)
	cloud.receivePacket(packet4)

	time = 100
	print "\ntest 2: should return 2 packets"

	for i in range(0,20):
		#print time
		packetList = cloud.updateTime(time)
		if packetList != None:
			print packetList[0].packet_id
		time = time + 1
	print "\n"

