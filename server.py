from socket import *
from threading import *
import time

def serverrecv():
	while 1:
		time.sleep(1)
		try:
			clientmsg=connectionsocket.recv(1024)
			if clientmsg.decode("utf8") == "hello":
				connectionsocket.send("hi there!".encode("utf8"))
			elif clientmsg.decode("utf8") == "time":
				connectionsocket.send(time.asctime(time.localtime(time.time())).encode("utf8"))
			elif clientmsg.decode("utf8") == "quit":
				connectionsocket.send("buh bye!".encode("utf8"))
				connectionsocket.close()
				exit(0)
			elif clientmsg.decode("utf8") == "help":
				connectionsocket.send("time: display time".encode("utf8"))
				connectionsocket.send("quit: kick yourself out".encode("utf8"))
				connectionsocket.send("help: display this message".encode("utf8"))
			print("client: "+clientmsg.decode("utf8"))
		except ConnectionAbortedError:
			print("kicked client!")
			exit(0)

servername=''
serverport=7000
def replay():
	global connectionsocket,addr
	serversocket=socket(AF_INET, SOCK_STREAM) #create socket

	serversocket.bind((servername, serverport)) #bind address and socket

	serversocket.listen(1) #listen
	connectionsocket,addr=serversocket.accept() #accept and create connection socket
	print("client connected!\n", addr)

	Thread(target=serverrecv).start()
	
	
replay()
while 1:
	time.sleep(1)
	rawdata=input('')
	if rawdata == "kick":
		connectionsocket.close()
		replay()
	else:
		try:
			connectionsocket.send(rawdata.encode("utf8"))
		except OSError:
			continue
connectionsocket.close()