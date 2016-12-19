import statistics
class Data(object):

	def __init__(self):
		self.d = {}

	def putSendTime(self, id, sendTime):
		if id not in self.d:
		    self.d[id] = { 'sendTime' : sendTime, 'finalTime' : None }
		else:
		    self.d[id]['sendTime'] = sendTime

	def putFinalTime(self, id, finalTime):
		if id not in self.d:
			self.d[id] = { 'sendTime' : None, 'finalTime' : finalTime }
		else:
			self.d[id]['finalTime'] = finalTime

	def rawData(self):
		return self.d

	def getSendTime(self, id):
		if id in self.d:
			return self.d[id]['sendTime']
		else:
			return None

	def getFinalTime(self, id):
		if id in self.d:
			return self.d[id]['finalTime']
		else:
			return None

	def latency(self, id):
		if id in self.d and self.getFinalTime(id) is not None \
				and self.getSendTime(id) is not None:
			return self.getFinalTime(id) - self.getSendTime(id)
		else:
			return None

	def latencyList(self):
		return [self.latency(x) for x in self.d.keys() \
				if self.latency(x) is not None]

	def averageLatency(self):
		latlist = self.latencyList()
		if len(latlist) > 0:
			return statistics.median(self.latencyList())
		else:
			return 0

	def numDropped(self):
		return len([self.getFinalTime(x) for x in self.d if self.getFinalTime(x) is None])
