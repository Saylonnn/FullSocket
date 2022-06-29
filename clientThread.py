import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, clientAdress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.clientAdress = clientAdress
        print("New connection added: ", clientAdress)
    def run(self):
        print("Connection from : ", self.clientAdress)
        size = 1024
        msg = ''
        while True:
            try:
                data = self.csocket.recv(size)
                if data:
                    print(data)
                else:
                    raise ConnectionError('Client disconnected')
            except:
                self.csocket.close()
                return False





    def send_data(self, data):
        try:
            self.csocket.sendall(bytes(data, 'utf-8'))
        except:
            raise ConnectionError("Client disconnected")