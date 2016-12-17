import random

class Location(object):
	
	calculator = None
	
	def __init__(self, location = None):
		if not Location.calculator:
			Location.calculator = LocationCalculator()

		self.city = location if location else random.choice(Location.calculator.locations)

	def propogationDelayFrom(self, location):
		return Location.calculator.getPropogation(self.city, location.city)

class LocationCalculator(object):

	def __init__(self):
		self.propogations = {}
		self.createPropogationMatrix()

	def addPropogation(self, c1, c2, delay):
		pair = (c1, c2) if c1 < c2 else (c2, c1)
		self.propogations[pair] = delay

	def getPropogation(self, c1, c2):
		if c1 == c2:
			return 5

		pair = (c1, c2) if c1 < c2 else (c2, c1)
		if pair in self.propogations:
			return self.propogations[pair]
			
		return None

	locations = {
		"Atlanta"
		"Austin", 
		"Cambridge", 
		"Chicago", 
		"Cleveland", 
		"Dallas", 
		"Denver", 
		"Detroit", 
		"Houston", 
		"Kansas City", 
		"Los Angeles", 
		"Nashville", 
		"New Orleans", 
		"New York", 
		"Orlando", 
		"Philadelphia", 
		"Phoenix", 
		"San Antonio", 
		"San Diego", 
		"San Francisco", 
		"St. Louis", 
		"Seattle", 
		"Washington"
	}

	def createPropogationMatrix(self):
		self.addPropogation("Atlanta", "Austin", 24)
		self.addPropogation("Atlanta", "Cambridge", 29)
		self.addPropogation("Atlanta", "Chicago", 26)
		self.addPropogation("Atlanta", "Cleveland", 19)
		self.addPropogation("Atlanta", "Dallas", 17)
		self.addPropogation("Atlanta", "Denver", 38)
		self.addPropogation("Atlanta", "Detroit", 23)
		self.addPropogation("Atlanta", "Houston", 23)
		self.addPropogation("Atlanta", "Kansas City", 25)
		self.addPropogation("Atlanta", "Los Angeles", 49)
		self.addPropogation("Atlanta", "Nashville", 8)
		self.addPropogation("Atlanta", "New Orleans", 12)
		self.addPropogation("Atlanta", "New York", 24)
		self.addPropogation("Atlanta", "Orlando", 11)
		self.addPropogation("Atlanta", "Philadelphia", 22)
		self.addPropogation("Atlanta", "Phoenix", 43)
		self.addPropogation("Atlanta", "San Antonio", 27)
		self.addPropogation("Atlanta", "San Diego", 48)
		self.addPropogation("Atlanta", "San Francisco", 60)
		self.addPropogation("Atlanta", "St. Louis", 20)
		self.addPropogation("Atlanta", "Seattle", 72)
		self.addPropogation("Atlanta", "Washington", 19)


if __name__ == "__main__":
	loc1 = Location("Atlanta")
	loc2 = Location("Denver")
	print "Distance from " + loc1.city + " to " + loc2.city + " is " + str(loc1.propogationDelayFrom(loc2))