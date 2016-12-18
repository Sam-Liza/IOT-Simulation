import cloud
import packet

if __name__ == "__main__":
	
    packet1 = packet.Packet(100, 0, 0, 1)
    packet2 = packet.Packet( 0, 0, 0, 2)
    packet3 = packet.Packet(100, 0, 0, 1)
    packet4 = packet.Packet( 100, 0, 0, 2)

    cloud = cloud.Cloud(0, 0, 10, 10)

    cloud.receiveRequest(packet1)
    cloud.receiveRequest(packet4)
    cloud.receiveRequest(packet3)
    cloud.receiveRequest(packet2)

    time = 100
    print "\ntest 1: should return 3 packets"
    for i in range(0,20):
    	#print time 
    	packetList = cloud.updateTime(time)
    	if packetList != None:
			print packetList[0].packet_id
        time = time + 1

    cloud.receiveRequest(packet1)
    cloud.receiveRequest(packet2)
    cloud.receiveRequest(packet3)
    cloud.receiveRequest(packet4)

    time = 100
    print "\ntest 2: should return 2 packets"

    for i in range(0,20):
    	#print time 
    	packetList = cloud.updateTime(time)
    	if packetList != None:
			print packetList[0].packet_id
        time = time + 1
    print "\n"

