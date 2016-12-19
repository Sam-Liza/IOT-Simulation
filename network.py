import random
from location import Location

class Network(object):

	def __init__(self, packet_loss_prob):
		self.packet_loss_prob = packet_loss_prob / 100.0
		pass

	def networkDelay(self, loc1, loc2):
		# Check for packet loss
		if random.random() < self.packet_loss_prob:
			return -1

		# Otherwise, return propagation delay
		return loc1.propagationDelayFrom(loc2)

class TCP(Network):

	TIMEOUT_RATE = 100 # ms
	HEADER_PROCESSING = 5 # ms

	def __init__(self, packet_loss_prob):
		super(TuftsSecure, self).__init__(packet_loss_prob)

	def networkDelay(self, loc1, loc2):
		propDelay = Network.networkDelay(loc1, loc2)
		propDelay += TCP.HEADER_PROCESSING
		if propDelay >= TCP.HEADER_PROCESSING:
			return propDelay * 2
		else:
			return TCP.TIMEOUT_RATE + self.networkDelay(loc1, loc2)

class UDP(Network):

	HEADER_PROCESSING = 2 # ms

	def __init__(self, packet_loss_prob):
		super(TuftsSecure, self).__init__(packet_loss_prob)

	def networkDelay(self, loc1, loc2):
		propDelay = Network.networkDelay(loc1, loc2)
		propDelay += UDP.HEADER_PROCESSING
		if propDelay >= UDP.HEADER_PROCESSING:
			return propDelay
		else:
			return 0

if __name__ == "__main__":

	loc1 = Location("Washington")
	loc2 = Location("Chicago")

	# Timeout test
	network = Network(2) # 2 percent chance to drop packet
	attempts = 0
	while network.networkDelay(loc1, loc2) != -1:
		attempts += 1
	print "Network dropped packet after " + str(attempts + 1) + " packets sent"
