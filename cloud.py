class Cloud(object):

	def __init__(self, processor, gpu):
		self.processor = processor
		self.gpu = gpu

	def processData(self, data):
		# Determine how much time it takes to process
		time = data / gpu

class AmazonWebService(Cloud):
	def __init__(self):
		super(AmazonWebService, self).__init__(3.5, 780)

clouds = {
	"aws" : AmazonWebService()
}