import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.117.230", 8485))
while True:
    data = client_socket.recv(1024)
    data = data.decode('utf-8')
    print(data)

