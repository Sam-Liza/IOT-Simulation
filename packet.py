import uuid

class Packet(object):

    def __init__(self, client_id, event_type, packet_size, timestamp):
        self._init_packet_id()
        self.client = client_id
        self.event = event_type
        self.size = packet_size
        self.timestamp = timestamp

    def _init_packet_id(self):
        self.unique_id = uuid.uuid4()
