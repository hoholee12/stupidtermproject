from socket import *

servername='127.0.0.1'
serverport=7000

clientsocket=socket(AF_INET, SOCK_STREAM) #create socket
clientsocket.connect((servername, serverport)) #connect => server.accept
print("connected.");
while 1:
	rawdata=input('input string: ')
	clientsocket.send(rawdata.encode("utf8")) #send
	rawdata=clientsocket.recv(1024) #receive
	print("from server: ", rawdata)
