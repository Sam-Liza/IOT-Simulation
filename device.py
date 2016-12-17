from game import Game
from packet import Packet

class Device(object):

	def __init__(self, deviceID, hwTier, eventsPerSec, location):
		self.deviceID = deviceID
		self.hwTier = hwTier
		self.eventsPerSec = eventsPerSec
		self.location = location

	def getSpecsForGame(game):
		pass

	def sendPacket():
		packet = Packet((5,50), , deviceID)

	def run():
		sendPacket()

		


class OculusRift(Device):
	def __init__(self, deviceID, hwTier, eventsPerSec, location):
		super(OculusRift, self).__init__(deviceID, 90, eventsPerSec, location)

class HTCVive(Device):
	def __init__(self, deviceID, hwTier, eventsPerSec, location):
		super(HTCVive, self).__init__(deviceID, 90, eventsPerSec, location)

class PlayStationVR(Device):
	def __init__(self, deviceID, hwTier, eventsPerSec, location):
		super(PlayStationVR, self).__init__(deviceID, 120, eventsPerSec, location)

class LG360VR(Device):
	def __init__(self, deviceID, hwTier, eventsPerSec, location):
		super(LG360VR, self).__init__(deviceID, 120, eventsPerSec, location)

class GearVR(Device):
	def __init__(self, deviceID, hwTier, eventsPerSec, location):
		super(GearVR, self).__init__(deviceID, 60, eventsPerSec, location)

class VisusVR(Device):
	def __init__(self, deviceID, hwTier, eventsPerSec, location):
		super(VisusVR, self).__init__(deviceID, 60, eventsPerSec, location)

devices = {
	"OculusRift" : OculusRift(),
	"HTCVive" : HTCVive(),
	"PlayStationVR" : PlayStationVR(),
	"SamsungGearVR" : SamsungGearVR(),
	"LG360VR" : LG360VR(),
	"VisusVR" : VisusVR(),
}