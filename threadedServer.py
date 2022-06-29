import socket
import threading
from clientThread import ClientThread

class ThreadedServer():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
        self.sock.bind((self.host, self.port))
        self.connections = []

    def listen(self, maxConnectedPorts=5):
        self.sock.listen(maxConnectedPorts)
        while True:
            client, address = self.sock.accept()
            #client.settimeout(60)
            conn = ClientThread(client, address)
            conn.start()
            self.connections.append(conn)

    def sendToAllString(self, data):
        for x in self.connections:
            try:
                x.sendData(data)
            except ConnectionError:
                print(x , " has disconnected.")
                self.connections.remove(x)
