from packet import Packet
from random import randint

TICKS_PER_EVENT = 20

class Device(object):

	def __init__(self, deviceID, fps, ticksPerEvent, location):
		self.deviceID = deviceID
		self.fps = fps
		self.ticksPerEvent = ticksPerEvent
		self.location = location
		
		self.position = (randint(0, 10), randint(5, 20))
		self.timeMS = 0
		self.packetDict = {}
	
	def updateTime(self, time, packet=None):
		if packet is None:
			return self.sendPacket(time)
		else:
			self.receivePacket(time, packet)


	def sendPacket(self, time):
		if time % self.ticksPerEvent == 0:
			self.movePlayer(time)
			packet = Packet(time, self.position, 0, self.deviceID)
			id = packet.packet_id
			self.packetDict[id] = {'sendTime' : time, 'receiveTime' : -1}
			print 'Device: %d.  Location: %s.  Packet sent: %s.  Timestamp: %s' % (self.deviceID, self.location, packet.packet_id, packet.timestamp)
			return packet
		return None

	def receivePacket(self, time, packet):
		print 'Device: %d.  Location: %s.  Packet received: %s.  Timestamp: %s' % (self.deviceID, self.location, packet.packet_id, packet.timestamp)
		id = packet.packet_id
		if id in self.packetDict.keys():
			self.packetDict[id]['receiveTime'] = time
		else:
			# stray packet received
			self.packetDict[id] = {'sendTime' : -1, 'receiveTime' : time}

	def movePlayer(self, time):
			self.position = (randint(0, 10), randint(5, 50))


class OculusRift(Device):
	def __init__(self, deviceID, location):
		super(OculusRift, self).__init__(deviceID, 90, TICKS_PER_EVENT, location)

class HTCVive(Device):
	def __init__(self, deviceID, location):
		super(HTCVive, self).__init__(deviceID, 90, TICKS_PER_EVENT, location)

class PlayStationVR(Device):
	def __init__(self, deviceID, location):
		super(PlayStationVR, self).__init__(deviceID, 120, TICKS_PER_EVENT, location)

class LG360VR(Device):
	def __init__(self, deviceID, location):
		super(LG360VR, self).__init__(deviceID, 120, TICKS_PER_EVENT, location)

class GearVR(Device):
	def __init__(self, deviceID, location):
		super(GearVR, self).__init__(deviceID, 60, TICKS_PER_EVENT, location)

class VisusVR(Device):
	def __init__(self, deviceID, location):
		super(VisusVR, self).__init__(deviceID, 60, TICKS_PER_EVENT, location)