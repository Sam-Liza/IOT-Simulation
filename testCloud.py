import cloud
import packet

if __name__ == "__main__":
	
    packet1 = packet.Packet(0, 100, 0, 0, 1)
    packet2 = packet.Packet(0, 100, 0, 0, 2)
    cloud = cloud.Cloud(0, 0, 10, 10)
    cloud.receiveRequest(packet1)

    cloud.receiveRequest(packet2)

    time = 90

    for i in range(0,10):
		time = time + 1
		packetList = cloud.updateTime(time)
		if packetList != None:
			print packetList[0].packet_id



