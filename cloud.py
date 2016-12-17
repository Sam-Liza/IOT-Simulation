import Queue

# these delays can be seen as the time response time of the server for each game
# being played 

HI_P_CLOUD_DELAY = 10  
MED_P_CLOUD_DELAY = 5
LOW_P_CLOUD_DELAY = 3
NUM_PLAYERS = 10
ks
class Cloud(object):

	def __init__(self, gameTraffic, location, timeout):
		
		self.requestList = Queue.Queue()

		if gameTraffic == 0: 
			self.timeToProcess = LOW_P_CLOUD_DELAY
		elif gameTraffic == 1: 
			self.timeToProcess = MED_P_CLOUD_DELAY
		else:
			self.timeToProcess = HIGH_P_CLOUD_DELAY

		self.location = location
		self.timeMS = 0
		self.timeout = timeout

	def updateTime(self, time):  # is this how it works? 
		self.timeMS = time
		return processResponse(self)

	def processResponse(self):

		if self.timeMS  % timeToProcess == 0 and not self.requestList.empty() :
			headPacket = self.requestList.get();
			if (time - headPacket.timestamp) >  timeout: 
				return None
			else: 
				responsePackets[]
				for i in range(1,NUM_PLAYERS):
					newPacket = headPacket

					# update packet 
					newPacket.sendAddress = 0
					newPacket.receiveAddress = i
					responsePackets[i].append(newPacket)
				return responsePackets
		else:
			return None

	def receiveRequest(self, packet):   # can this access 
		self.requestList.put(packet)

