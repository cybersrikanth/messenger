import socket
s=socket.socket()
host="127.0.0.1"
port=450
s.bind((host,port))
s.listen(5)
print("Local server started successfully")
print("******************CYBERSRIKANTH********************")
def sndmsg():
    while True:
        c, addr=s.accept()
        print ("got connection from" ,addr)
        msg=input("Enter the message:")
        c.send(msg.encode())
        c.close()
sndmsg()
