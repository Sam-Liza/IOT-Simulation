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
		"Denver", 
		"New York", 
		"Orlando", 
		"Philadelphia", 
		"San Francisco", 
		"Seattle", 
		"Washington"
	}

	def createPropogationMatrix(self):
		self.addPropogation("Atlanta", "Austin", 24)
		self.addPropogation("Atlanta", "Cambridge", 29)
		self.addPropogation("Atlanta", "Chicago", 26)
		self.addPropogation("Atlanta", "Denver", 38)
		self.addPropogation("Atlanta", "New York", 24)
		self.addPropogation("Atlanta", "Orlando", 11)
		self.addPropogation("Atlanta", "Philadelphia", 22)
		self.addPropogation("Atlanta", "San Francisco", 60)
		self.addPropogation("Atlanta", "Seattle", 72)
		self.addPropogation("Atlanta", "Washington", 19)

		self.addPropogation("Austin", "Cambridge", 52)
		self.addPropogation("Austin", "Chicago", 33)
		self.addPropogation("Austin", "Denver", 25)
		self.addPropogation("Austin", "New York", 45)
		self.addPropogation("Austin", "Orlando", 28)
		self.addPropogation("Austin", "Philadelphia", 46)
		self.addPropogation("Austin", "San Francisco", 49)
		self.addPropogation("Austin", "Seattle", 58)
		self.addPropogation("Austin", "Washington", 40)

		self.addPropogation("Cambridge", "Chicago", 27)
		self.addPropogation("Cambridge", "Denver", 47)
		self.addPropogation("Cambridge", "New York", 6)
		self.addPropogation("Cambridge", "Orlando", 40)
		self.addPropogation("Cambridge", "Philadelphia", 9)
		self.addPropogation("Cambridge", "San Francisco", 76)
		self.addPropogation("Cambridge", "Seattle", 72)
		self.addPropogation("Cambridge", "Washington", 11)

		self.addPropogation("Chicago", "Denver", 21)
		self.addPropogation("Chicago", "New York", 20)
		self.addPropogation("Chicago", "Orlando", 37)
		self.addPropogation("Chicago", "Philadelphia", 18)
		self.addPropogation("Chicago", "San Francisco", 50)
		self.addPropogation("Chicago", "Seattle", 47)
		self.addPropogation("Chicago", "Washington", 22)

		self.addPropogation("Denver", "New York", 42)
		self.addPropogation("Denver", "Orlando", 46)
		self.addPropogation("Denver", "Philadelphia", 39)
		self.addPropogation("Denver", "San Francisco", 30)
		self.addPropogation("Denver", "Seattle", 34)
		self.addPropogation("Denver", "Washington", 42)

		self.addPropogation("New York", "Orlando", 35)
		self.addPropogation("New York", "Philadelphia", 4)
		self.addPropogation("New York", "San Francisco", 71)
		self.addPropogation("New York", "Seattle", 68)
		self.addPropogation("New York", "Washington", 5)

		self.addPropogation("Orlando", "Philadelphia", 33)
		self.addPropogation("Orlando", "San Francisco", 68)
		self.addPropogation("Orlando", "Seattle", 81)
		self.addPropogation("Orlando", "Washington", 30)

		self.addPropogation("Philadelphia", "San Francisco", 68)
		self.addPropogation("Philadelphia", "Seattle", 64)
		self.addPropogation("Philadelphia", "Washington", 30)

		self.addPropogation("San Francsico", "Seattle", 60)
		self.addPropogation("San Francsico", "Washington", 41)

		self.addPropogation("Washington", "Seattle", 68)

if __name__ == "__main__":
	loc1 = Location("Washington")
	loc2 = Location("Chicago")
	print "Delay from " + loc1.city + " to " + loc2.city + " is " + str(loc1.propogationDelayFrom(loc2)) + " ms"