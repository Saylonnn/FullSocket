import socket
import threading


class ThreadedServer():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket created")

        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        print("Socket binded")
        self.connections = []

    def listen(self, maxConnectedPorts=5):
        self.sock.listen(maxConnectedPorts)
        while True:
            client, address = self.sock.accept()
            print("Accepted ", address)
            self.connections.append(client)
            threading.Thread(target = self.listenToClient, args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    print(data)

            except ConnectionError:
                client.close()
                return False

    def send_to_all_string(self, data):
        for x in self.connections:
            try:
                x.sendData(data)
            except ConnectionError:
                print(x, " has disconnected.")
                self.connections.remove(x)
