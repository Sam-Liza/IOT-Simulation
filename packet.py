import uuid
import heapq

class Packet(object):

    def __init__(self, timestamp, receiver, sender, packet_id = None):
        self.packet_id = packet_id if packet_id is not None else uuid.uuid4()
        self.timestamp = timestamp
        self.receiver = receiver
        self.sender = sender
        self.elapsedTime = 0

    def addLatency(self, elapsedTime):
        self.elapsedTime += elapsedTime

    def isReady(self, time):
        return self.arriveTime() >= time

    def arriveTime(self):
        return self.timestamp + self.elapsedTime

    def deepcopy(self):
        return Packet(self.timestamp, self.receiver, self.sender, self.packet_id)

# Packet priority queue, with packets ordered by arrival time
class PacketQueue(object):

    def __init__(self):
        self._packets = []

    def push(self, packet):
        toAdd = (packet.arriveTime(), packet)
        heapq.heappush(self._packets, toAdd)

    def pop(self):
        return (heapq.heappop(self._packets))[1]

    def next(self):
        return self._packets[0][1]

    def empty(self):
        return len(self._packets) == 0

