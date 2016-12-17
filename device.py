from game import Game
from packet import Packet
import Cloud

class Device(object):

	def __init__(self, deviceID, hwTier, eventsPerSec, location):
		self.deviceID = deviceID
		self.hwTier = hwTier
		self.eventsPerSec = eventsPerSec
		self.location = location
		self.position = (deviceID * 5, deviceID * 10)
		self.timeMS = 0

	def updateTime(self, time):
		self.timeMS = time
		movePlayer(time)
		return processResponse(self)

	def processResponse():
		if self.timeMS  % self.eventsPerSec == 0:
			packet = Packet(self.position, self.timeMS, 0, self.deviceID)
			return packet
		return None

	def movePlayer(time):
		


class OculusRift(Device):
	def __init__(self, deviceID, location):
		super(OculusRift, self).__init__(deviceID, 90, 5, location)

class HTCVive(Device):
	def __init__(self, deviceID, location):
		super(HTCVive, self).__init__(deviceID, 90, 5, location)

class PlayStationVR(Device):
	def __init__(self, deviceID, location):
		super(PlayStationVR, self).__init__(deviceID, 120, 5, location)

class LG360VR(Device):
	def __init__(self, deviceID, location):
		super(LG360VR, self).__init__(deviceID, 120, 5, location)

class GearVR(Device):
	def __init__(self, deviceID, location):
		super(GearVR, self).__init__(deviceID, 60, 5, location)

class VisusVR(Device):
	def __init__(self, deviceID, location):
		super(VisusVR, self).__init__(deviceID, 60, 5, location)

devices = {
	"OculusRift" : OculusRift(),
	"HTCVive" : HTCVive(),
	"PlayStationVR" : PlayStationVR(),
	"SamsungGearVR" : SamsungGearVR(),
	"LG360VR" : LG360VR(),
	"VisusVR" : VisusVR(),
}