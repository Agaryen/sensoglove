import socket
from .hand import Hand

from .helpers import read_json_payload


class SensoGlove:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection_error = None
        self.hand = None
        self.src = None
        self.name = None
        self.battery = None
        self.temperature = None

    def _init_header_props(self):
        data = None
        while data is None:
            data = read_json_payload(self.socket)
            self.src = data['src']
            self.name = data['name']

    def connect(self):
        try:
            self.socket.connect((self.host, self.port))
            self._init_header_props()
        except ConnectionRefusedError as err:
            self.connection_error = err
            raise

    def set_data(self):
        data = read_json_payload(self.socket)
        if data is None:
            return
        self.hand = Hand(data)
        self.battery = data['battery']
        self.temperature = data['temperature']
