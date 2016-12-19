import random
from location import Location

class Network(object):

	def __init__(self, packet_loss_prob):
		self.packet_loss_prob = packet_loss_prob / 100.0
		pass

	def networkDelay(self, loc1, loc2):
		# Check for packet loss
		if random.random() < self.packet_loss_prob:
			return None

		# Otherwise, return propagation delay
		return loc1.propagationDelayFrom(loc2)

class TCP(Network):

	TIMEOUT_RATE = 100 # ms
	HEADER_PROCESSING = 5 # ms

	def __init__(self, packet_loss_prob):
		super(TCP, self).__init__(packet_loss_prob)

	def networkDelay(self, loc1, loc2):
		propDelay = super(TCP, self).networkDelay(loc1, loc2)
		if propDelay is not None:
			propDelay += self.HEADER_PROCESSING
			return propDelay * 2
		else:
			return None

class UDP(Network):

	HEADER_PROCESSING = 2 # ms

	def __init__(self, packet_loss_prob):
		super(UDP, self).__init__(packet_loss_prob)

	def networkDelay(self, loc1, loc2):
		propDelay = super(UDP, self).networkDelay(loc1, loc2)
		if propDelay is not None:
			return propDelay + self.HEADER_PROCESSING
		else:
			return None
