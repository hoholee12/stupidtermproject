from socket import *
from threading import *

def clientrecv():
	while 1:
		servermsg=clientsocket.recv(1024)
		if servermsg:
			print("server: "+servermsg.decode("utf8"))
		else:
			clientsocket.close()
			exit(0)

	


servername='127.0.0.1'
serverport=7000

clientsocket=socket(AF_INET, SOCK_STREAM) #create socket
clientsocket.connect((servername, serverport)) #connect => server.accept
print("connected.");

Thread(target=clientrecv).start()

while 1:
	rawdata=input('')
	try:
		clientsocket.send(rawdata.encode("utf8")) #send
	except OSError:
		exit(0)