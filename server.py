from socket import *
from threading import *

def serverrecv():
	while 1:
		clientmsg=connectionsocket.recv(1024)
		print("client: "+clientmsg.decode("utf8"))


servername=''
serverport=7000

serversocket=socket(AF_INET, SOCK_STREAM) #create socket

serversocket.bind((servername, serverport)) #bind address and socket

serversocket.listen(1) #listen
connectionsocket,addr=serversocket.accept() #accept and create connection socket
print("client connected!\n", addr)
	
Thread(target=serverrecv).start()
	
while 1:
	#rawdata=connectionsocket.recv(1024) #receive
	#print(rawdata)
	#connectionsocket.send(rawdata.upper()) #send
	rawdata=input()
	connectionsocket.send(rawdata.encode("utf8"))
	
connectionsocket.close()