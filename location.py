import random

class Location(object):

	calculator = None

	def __init__(self, location = None):
		if not Location.calculator:
			Location.calculator = LocationCalculator()

		self.city = location if location else random.choice(Location.calculator.locations)

	def propagationDelayFrom(self, location):
		return Location.calculator.getPropagation(self.city, location.city)

class LocationCalculator(object):

	def __init__(self):
		self.propagations = {}
		self.createPropagationMatrix()

	def addPropagation(self, c1, c2, delay):
		pair = (c1, c2) if c1 < c2 else (c2, c1)
		self.propagations[pair] = delay

	def getPropagation(self, c1, c2):
		if c1 == c2:
			return 5

		pair = (c1, c2) if c1 < c2 else (c2, c1)
		if pair in self.propagations:
			return self.propagations[pair]

		return None

	locations = {
		"Atlanta",
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

	def createPropagationMatrix(self):
		self.addPropagation("Atlanta", "Austin", 24)
		self.addPropagation("Atlanta", "Cambridge", 29)
		self.addPropagation("Atlanta", "Chicago", 26)
		self.addPropagation("Atlanta", "Denver", 38)
		self.addPropagation("Atlanta", "New York", 24)
		self.addPropagation("Atlanta", "Orlando", 11)
		self.addPropagation("Atlanta", "Philadelphia", 22)
		self.addPropagation("Atlanta", "San Francisco", 60)
		self.addPropagation("Atlanta", "Seattle", 72)
		self.addPropagation("Atlanta", "Washington", 19)

		self.addPropagation("Austin", "Cambridge", 52)
		self.addPropagation("Austin", "Chicago", 33)
		self.addPropagation("Austin", "Denver", 25)
		self.addPropagation("Austin", "New York", 45)
		self.addPropagation("Austin", "Orlando", 28)
		self.addPropagation("Austin", "Philadelphia", 46)
		self.addPropagation("Austin", "San Francisco", 49)
		self.addPropagation("Austin", "Seattle", 58)
		self.addPropagation("Austin", "Washington", 40)

		self.addPropagation("Cambridge", "Chicago", 27)
		self.addPropagation("Cambridge", "Denver", 47)
		self.addPropagation("Cambridge", "New York", 6)
		self.addPropagation("Cambridge", "Orlando", 40)
		self.addPropagation("Cambridge", "Philadelphia", 9)
		self.addPropagation("Cambridge", "San Francisco", 76)
		self.addPropagation("Cambridge", "Seattle", 72)
		self.addPropagation("Cambridge", "Washington", 11)

		self.addPropagation("Chicago", "Denver", 21)
		self.addPropagation("Chicago", "New York", 20)
		self.addPropagation("Chicago", "Orlando", 37)
		self.addPropagation("Chicago", "Philadelphia", 18)
		self.addPropagation("Chicago", "San Francisco", 50)
		self.addPropagation("Chicago", "Seattle", 47)
		self.addPropagation("Chicago", "Washington", 22)

		self.addPropagation("Denver", "New York", 42)
		self.addPropagation("Denver", "Orlando", 46)
		self.addPropagation("Denver", "Philadelphia", 39)
		self.addPropagation("Denver", "San Francisco", 30)
		self.addPropagation("Denver", "Seattle", 34)
		self.addPropagation("Denver", "Washington", 42)

		self.addPropagation("New York", "Orlando", 35)
		self.addPropagation("New York", "Philadelphia", 4)
		self.addPropagation("New York", "San Francisco", 71)
		self.addPropagation("New York", "Seattle", 68)
		self.addPropagation("New York", "Washington", 5)

		self.addPropagation("Orlando", "Philadelphia", 33)
		self.addPropagation("Orlando", "San Francisco", 68)
		self.addPropagation("Orlando", "Seattle", 81)
		self.addPropagation("Orlando", "Washington", 30)

		self.addPropagation("Philadelphia", "San Francisco", 68)
		self.addPropagation("Philadelphia", "Seattle", 64)
		self.addPropagation("Philadelphia", "Washington", 30)

		self.addPropagation("San Francsico", "Seattle", 60)
		self.addPropagation("San Francsico", "Washington", 41)

		self.addPropagation("Seattle", "Washington", 68)

if __name__ == "__main__":
	loc1 = Location("Washington")
	loc2 = Location("Chicago")
	print "Delay from " + loc1.city + " to " + loc2.city + " is" \
	, str(loc1.propagationDelayFrom(loc2)) + " ms"
