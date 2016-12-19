import uuid

class Packet(object):

    def __init__(self, timestamp, receiver, sender):
        self._init_packet_id()
        self.timestamp = timestamp
        self.receiver = receiver
        self.sender = sender
        self.elapsedTime = 0
        self.phase = 'network->cloud'

    def _init_packet_id(self):
        self.packet_id = uuid.uuid4()	# generate a random UUID

    def addLatency(self, elapsedTime):
        self.elapsedTime += elapsedTime

    def isReady(self, time):
        return self.timestamp + self.elapsedTime >= time

    def arriveTime(self):
        return self.timestamp + self.elapsedTime

