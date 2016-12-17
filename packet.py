import uuid

class Packet(object):

    def __init__(self, event, timestamp, position, receiverAddress, senderAddress):
        self._init_packet_id()
        self.event = event
        self.timestamp = timestamp
        self.position = position
        self.receiverAddress = receiverAddress
        self.senderAddress = senderAddress

    def _init_packet_id(self):
        self.packet_id = uuid.uuid4()	# generate a random UUID