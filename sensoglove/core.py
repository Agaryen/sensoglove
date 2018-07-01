import socket


class SensoGlove:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection_error = None

    def connect(self):
        try:
            self.socket.connect((self.host, self.port))
        except ConnectionRefusedError as err:
            self.connection_error = err
