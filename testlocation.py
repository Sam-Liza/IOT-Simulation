from location import Location

if __name__ == "__main__":
	loc1 = Location("Washington")
	loc2 = Location("Chicago")
	print "Delay from " + loc1.city + " to " + loc2.city + " is" \
	+ str(loc1.propagationDelayFrom(loc2)) + " ms"

