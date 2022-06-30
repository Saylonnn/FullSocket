import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((str(socket.gethostbyname(socket.gethostname())), 8485))
client_socket.connect(("192.168.117.230", 8485))
print("connected")
while True:
    data = client_socket.recv(1024)
    data = data.decode('utf-8')
    print("data: ", data)

