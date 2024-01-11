import socket
import time

#NB: Alternative to reading contents from the internet is by using the urllib module.

'''
#CREATE A SOCKET.        NB: You need internet connection
sockObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockObject.connect(("www.google.com",80))
'''


#CREATE A SOCKET.        NB: You need internet connection
sockObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockObject.connect(('data.pr4e.org',80))        #NB: Remove http(s)

#Send command to receive data
command = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()        #NB .encode() encodes from Unicode to UTF-8
sockObject.send(command)
print("Commmand sent")
time.sleep(3)
print("Receiving data in...")
for i in range(3,0,-1):
    print(i, end="\n")
    time.sleep(1)
time.sleep(1)

#Receive and parse data
while True:
    data = sockObject.recv(512)     #Receives upto 512 characters
    if(len(data) < 1):
        break
    print(data.decode())            #Decodes from UTF-8 to Unicode
sockObject.close()

#NB: urllib module can be used to achieve this as well, perhaps easier