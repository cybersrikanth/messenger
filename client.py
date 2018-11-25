import time
import socket
while True:
    s=socket.socket()
    host="127.0.0.1"
    port=450
    s.connect((host,port))
    print(s.recv(1000).decode())
    time.sleep(5)
