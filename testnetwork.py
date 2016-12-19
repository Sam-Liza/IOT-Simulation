from network import Network
from location import Location

if __name__ == "__main__":

	loc1 = Location("Washington")
	loc2 = Location("Chicago")

	# Timeout test
	network = Network(2) # 2 percent chance to drop packet
	attempts = 0
	while network.networkDelay(loc1, loc2) != None:
		attempts += 1
	print "Network dropped packet after " + str(attempts + 1) + " packets sent"
