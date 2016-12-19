import statistics
class Data(object):

	def __init__(self):
		self.d = {}

	def putSend(self, id, sendTime):
		if id not in self.d:
		    self.d[id] = { 'sendTime' : sendTime, 'receiveTime' : None }
		else:
		    self.d[id]['sendTime'] = sendTime

	def putReceive(self, id, receiveTime):
		print "received: " + str(id) + ", " + str(receiveTime)
		if id not in self.d:
		    self.d[id] = { 'sendTime' : None, 'receiveTime' : receiveTime }
		else:
		    self.d[id]['receiveTime'] = receiveTime

	def rawData(self):
		return self.d

	def sendTime(self, id):
		return self.d[id]['sendTime']

	def receiveTime(self, id):
		return self.d[id]['receiveTime']

	def latency(self, id):
		if self.receiveTime(id) is not None and self.sendTime(id) is not None:
			return self.d[id]['receiveTime'] - self.d[id]['sendTime']
		else:
			return None

	def latencyList(self):
		return [self.latency(x) for x in self.d.keys() if self.latency(x) is not None]

	def averageLatency(self):
		return statistics.median(self.latencyList())

	def numDropped(self):
		return len([self.receiveTime(x) for x in self.d if self.receiveTime(x) is None])
