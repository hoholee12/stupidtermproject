from tkinter import *
from tkinter.filedialog import asksaveasfilename
import threading
import socket
from sys import *

#global vars
username="me"
connectionsocket=0

#my crypto technique
secretkey="badasscryptography"

encrypt_on=0
decrypt_on=0

def togglecfg(set):
	global encrypt_on
	global decrypt_on
	if set == 0: #decrypt switch
		if encrypt_on == 0:
			encrypt_on=1
		else:
			encrypt_on=0
	if set == 1: #decrypt switch
		if decrypt_on == 0:
			decrypt_on=1
		else:
			decrypt_on=0

def encrypt(result):
	multiplication=0
	p=0
	for c in secretkey:
		p+=1
		multiplication=multiplication+(p*ord(str(c)))
		
	stuff="1337"
	stuff=stuff+str(1337*multiplication)
	stuff=stuff+","
	for j in range(0,len(result)):
		stuff=stuff+str(multiplication*ord(result[j]))
		try:
			if result[j+1]:
				stuff=stuff+","
		except IndexError:
			pass
			
	return stuff

def decrypt(stuff):
	if not "1337" in stuff:
		print("its not mine.") #exception
		return stuff
	i=stuff.replace('1337','')
	i=i.split(',')
	multiplication=0
	p=0
	for c in secretkey:
		p+=1
		multiplication=multiplication+(p*ord(str(c)))
	if not str(multiplication*1337) in i[0]:
		print("incorrect password!")
		exit()
	i.pop(0)
	result=""
	for j in i:
		result=result+chr(int(int(j)/multiplication))
		
	return result



#menu funcs

#file
def savehistory():
	file_name=asksaveasfilename(title="save chat", filetypes=[('plain text', '*.txt'), ('any file', '*.*')])
	try:
		filehandle=open(file_name+".txt", "w")
	except IOError:
		print("failed to save!")
		return
	contents=main_body_text.get(1.0, END)
	for line in contents:
		filehandle.write(line)
	filehandle.close()
	
def username_options_window(master):
	top=Toplevel(master)
	top.title("username option")
	top.grab_set() #limit event to this window
	Label(top, text="username:").grid(row=0)
	name=Entry(top)
	name.focus_set() #focus window
	name.grid(row=0, column=1)
	go=Button(top, text="modify", command=lambda:username_options_go(name.get(), top))
	go.grid(row=1, column=0, columnspan=2, sticky=W+E) #center of first row
	
def username_options_go(name, window):
	for letter in [name]:
		if letter==" " or letter=="\n":
			error_window(root, "bad username, no spaces allowed!")
			return
	global username
	username=name
	writetoscreen("modified username: "+name, "system") #write to text widget on screen
	window.destroy()
	
def server_options_window(master):
	top=Toplevel(master)
	top.title("server port option")
	top.grab_set() #limit event to this window
	top.protocol("WM_DELETE_WINDOW", lambda:optiondelete(top))
	Label(top, text="port: ").grid(row=0)
	port=Entry(top)
	port.grid(row=0, column=1)
	port.focus_set() #focus window
	go=Button(top, text="start", command=lambda:server_options_go(port.get(), top))
	go.grid(row=1, column=1)
	
def server_options_go(port, window):
	if options_sanitation(port): #sanitizer
		window.destroy()
		server(int(port)).start() #start server thread
		
def optiondelete(window):
	connector.config(state=NORMAL) #enable connect button
	window.destroy()
	
def exitchat(window):
	if connectionsocket != 0:
		connectionsocket.close()
	if clienttype == 1:
		serv.close()
	window.destroy()
	
def client_options_window(master):
	top=Toplevel(master)
	top.title("client connection settings")
	top.protocol("WM_DELETE_WINDOW", lambda: optiondelete(top))
	top.grab_set() #limit event to this window
	Label(top, text="server IP:").grid(row=0)
	location=Entry(top)
	location.grid(row=0, column=1)
	location.focus_set() #focus window
	Label(top, text="port:").grid(row=1)
	port=Entry(top)
	port.grid(row=1, column=1)
	go=Button(top, text="start", command=lambda: client_options_go(location.get(), port.get(), top))
	go.grid(row=2, column=1)
	
def client_options_go(dest, port, window):
	if options_sanitation(port, dest): #sanitizer
		window.destroy()
		client(dest, int(port)).start() #start client thread
		
def options_sanitation(por, loc=""):
	if not por.isnumeric():
		error_window(root, "insert port number")
		return False
	if int(por) < 0 or 65555 < int(por):
		error_window(root, "range must be between 0~65555")
		return False
	if loc != "":
		if not ip_process(loc.split(".")):
			error_window(root, "insert a proper IP address")
			return False
	return True
	
def ip_process(iparray):
	if len(iparray) != 4:
		return False
	for ip in iparray:
		if not ip.isnumeric():
			return False
		t=int(ip)
		if t<0 or 255<t:
			return False
	return True

def error_window(master, texty):
	window=Toplevel(master)
	window.title("error")
	window.grab_set()
	Label(window, text=texty).pack()
	go=Button(window, text="ok", command=window.destroy)
	go.pack()
	go.focus_set() #focus window
	
def connects(clienttype):
	connector.config(state=DISABLED)
	if clienttype == 0:
		client_options_window(root)
	if clienttype == 1:
		server_options_window(root)
		
def toone():
	global clienttype
	clienttype=0
	
def totwo():
	global clienttype
	clienttype=1
	
def processusertext(event):
	data=text_input.get()
	placetext(data)
	text_input.delete(0, END)
	
def placetext(text):
	writetoscreen(text, username)
	netthrow(connectionsocket, text)
	
def writetoscreen(text, username=""):
	main_body_text.config(state=NORMAL)
	main_body_text.insert(END, '\n')
	if username:
		main_body_text.insert(END, "["+username+"]")
	main_body_text.insert(END, text)
	main_body_text.yview(END)
	main_body_text.config(state=DISABLED)
	
def netthrow(conn, message):
	try:
		if encrypt_on == 1: #if encrypt switch is on
			conn.send(encrypt(message).encode("utf8"))
		else:
			conn.send(message.encode("utf8"))
	except socket.error:
		writetoscreen("failed to send msg", "system")
		
def netcatch(conn):
	try:
		message=conn.recv(1024) #bigger buffer size to accept huge encrypted numbers
		if decrypt_on == 1:
			return decrypt(message.decode("utf8"))
		else:
			return message.decode("utf8")
	except socket.error:
		writetoscreen("failed to receive msg", "system")
		
class server(threading.Thread):
	def __init__(self, port):
		threading.Thread.__init__(self)
		self.port=port
	
	def run(self):
		global serv
		serv=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		serv.bind(('', self.port))
		serv.listen(1)
		global connectionsocket
		writetoscreen("waiting from port"+str(self.port)+"...", "system")
		connectionsocket,addr=serv.accept()
		writetoscreen("connected to"+str(addr[0]), "system")
		threading.Thread(target=runner, args=(connectionsocket,str(addr[0]))).start()
		
class client(threading.Thread):
	def __init__(self, host, port):
		threading.Thread.__init__(self)
		self.port=port
		self.host=host
	
	def run(self):
		global connectionsocket
		connectionsocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connectionsocket.connect((self.host, self.port))
		writetoscreen("connected to IP:"+self.host+"port:"+str(self.port), "system")
		
		threading.Thread(target=runner, args=(connectionsocket, self.host)).start()
		
def runner(conn, addr):
	while 1:
		data=netcatch(conn)
		writetoscreen(data, addr)
		
root=Tk()
root.title("GUI 채팅")

menubar=Menu(root)
root.config(menu=menubar)
file_menu=Menu(menubar, tearoff=0) #tearoff=0 removes dotted line
menubar.add_cascade(label="file", menu=file_menu)
file_menu.add_command(label="save", command=lambda: savehistory())
file_menu.add_command(label="username", command=lambda:username_options_window(root))
file_menu.add_command(label="exit", command=lambda: exitchat(root))
crypt_menu=Menu(menubar, tearoff=0) #tearoff=0 removes dotted line
menubar.add_cascade(label="crypt", menu=crypt_menu)
crypt_menu.add_command(label="encrypt output", command=lambda: togglecfg(0))
crypt_menu.add_command(label="decrypt input", command=lambda: togglecfg(1))



main_body=Frame(root) #main display
#text left side
main_body_text=Text(main_body)
main_body_text.pack(side=LEFT, fill=Y)
#scroller right side
body_text_scroll=Scrollbar(main_body)
body_text_scroll.pack(side=RIGHT, fill=Y)
#bind them
body_text_scroll.config(command=main_body_text.yview)
main_body_text.config(yscrollcommand=body_text_scroll.set)
main_body.pack()

main_body_text.insert(END, "welcome")
main_body_text.config(state=DISABLED) #disable text

#bottom corner
text_input=Entry(root, width=60)
text_input.bind("<Return>", processusertext)
text_input.pack()

clienttype=1
Radiobutton(root, text="client", variable=clienttype, value=0, command=toone).pack(anchor=E)
Radiobutton(root, text="server", variable=clienttype, value=0, command=totwo).pack(anchor=E)

statusconnect=StringVar()
statusconnect.set("connect")
connector=Button(root, textvariable=statusconnect, command=lambda: connects(clienttype))
connector.pack()

root.mainloop()