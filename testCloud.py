import cloud
import packet

if __name__ == "__main__":
	
def __init__(self, packet_id, event, timestamp, receiverAddress, senderAddress):
        self._init_packet_id()
        self.event = event
        self.timestamp = timestamp
        self.position = position
        self.receiverAddress = receiverAddress
        self.senderAddress = senderAddress


    packet1 = packet()


	packet1.id = 0
	packet1.sendAddress = 1
	packet1.receiveAddress = 0
	packet1.timestamp = 100
	packet2.id = 1
	packet2.sendAddress = 2
	packet2.receiveAddress = 0
	packet2.timestamp = 0

	cloud = Cloud(0, 0, 10)

	cloud.receiveRequest(packet1)
	cloud.receiveRequest(packet2)

	time = 90

	for i in range(0,10):
		time = time + 1
		packetList = cloud.updateTime(time)
		if packetList != None:
			print packetList[0].id



