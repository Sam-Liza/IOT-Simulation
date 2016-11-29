from game import Game

class Device(object):

	def __init__(self, ram, processor):
		self.processor = processor
		self.ram = ram

	def getSpecsForGame(game):
		pass

class OculusRift(Device):
	def __init__(self):
		super(OculusRift, self).__init__(3.5, 780)

devices = {
	"rift" : OculusRift()
}