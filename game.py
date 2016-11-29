class Game(object):

	def __init__(self, ramReqs, processorReqs):
		self.ramReqs = ramReqs
		self.processorReqs = processorReqs

class FarCry4(Game):
	def __init__(self):
		super(FarCry4, self).__init__(3.5, 780)

games = {
	"farcry" : FarCry4()
}