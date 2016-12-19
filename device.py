from packet import Packet
from random import randint
from data import Data

TICKS_PER_EVENT = 500

class Device(object):
	cloud_id = 0
	rendering_time = 5 #ms

	def __init__(self, fps, ticksPerEvent, location):
		self.fps = fps
		self.ticksPerEvent = ticksPerEvent
		self.firstEventOffset = randint(0, ticksPerEvent - 1)
		self.location = location
		self.data = Data()
		self.time = 0

	def step(self):
		self.time += 1
		if self.time % self.ticksPerEvent == self.firstEventOffset:
			packet = Packet(self.time, Device.cloud_id, self.id)
			id = packet.packet_id
			self.data.putSendTime(id, self.time)
			return [packet]
		else:
			return []

	def receivePacket(self, packet):
		id = packet.packet_id
		finalTime = packet.arriveTime() + Device.rendering_time
		self.data.putFinalTime(id, finalTime)

class OculusRift(Device):
	def __init__(self, location):
		super(OculusRift, self).__init__(90, TICKS_PER_EVENT, location)

class HTCVive(Device):
	def __init__(self, location):
		super(HTCVive, self).__init__(90, TICKS_PER_EVENT, location)

class PlayStationVR(Device):
	def __init__(self, location):
		super(PlayStationVR, self).__init__(120, TICKS_PER_EVENT, location)

class LG360VR(Device):
	def __init__(self, location):
		super(LG360VR, self).__init__(120, TICKS_PER_EVENT, location)

class GearVR(Device):
	def __init__(self, location):
		super(GearVR, self).__init__(60, TICKS_PER_EVENT, location)

class VisusVR(Device):
	def __init__(self, location):
		super(VisusVR, self).__init__(60, TICKS_PER_EVENT, location)
