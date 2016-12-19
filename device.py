from packet import Packet
from random import randint
from data import Data

TICKS_PER_EVENT = 20

class Device(object):

	def __init__(self, deviceID, fps, ticksPerEvent, location):
		self.deviceID = deviceID
		self.fps = fps
		self.ticksPerEvent = ticksPerEvent
		self.firstEventOffset = randint(0, ticksPerEvent - 1)
		self.location = location
		self.data = Data()

	def responseAt(self, time):
		if (time + self.firstEventOffset) % self.ticksPerEvent == 0:
			packet = Packet(time, 0, self.deviceID)
			id = packet.packet_id
			self.data.putSend(id, time)
			print 'Device: %d.  Location: %s.  Packet sent: %s.  Timestamp: %s' % (self.deviceID, self.location, packet.packet_id, packet.timestamp)
			return [packet]
		else:
			return []

	def receivePacket(packet):
		id = packet.packet_id
		arrival = packet.arriveTime()
		self.data.putReceive(id, arrival)
		print 'Device: %d.  Location: %s.  Packet received: %s.  Timestamp: %s' % (self.deviceID, self.location, packet.packet_id, packet.timestamp)


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
