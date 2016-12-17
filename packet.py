import uuid

class Packet(object):

    def __init__(self, timestamp, position, receiverAddress, senderAddress):
        self._init_packet_id()
        self.timestamp = timestamp
        self.position = position
        self.receiverAddress = receiverAddress
        self.senderAddress = senderAddress

    def _init_packet_id(self):
        self.packet_id = uuid.uuid4()	# generate a random UUID

    @property
    def packet_id(self):
        return self.packet_id