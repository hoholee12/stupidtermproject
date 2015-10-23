from socket import *

servername=''
serverport=7000

serversocket=socket(AF_INET, SOCK_STREAM) #create socket

serversocket.bind((servername, serverport)) #bind address and socket

serversocket.listen(1) #listen

while 1:
	connectionsocket,addr=serversocket.accept() #accept and create connection socket
	print("client connected! ", addr)
	rawdata=connectionsocket.recv(1024) #receive
	print(rawdata)
	connectionsocket.send(rawdata.upper()) #send
