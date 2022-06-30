import threading
import socket
import numpy as np
import sys
import pickle
from threadedServer import ThreadedServer

name = socket.gethostname()
print(name)
local_ip = socket.gethostbyname(name)
print(local_ip)

ts = ThreadedServer(local_ip, 8485)
ts.listen()