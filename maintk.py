#!/cygdrive/c/Python34/python.exe

from tkinter import *

app=Tk() #window

#label
'''
label=Label(app, text="hello world!") #label widget

label.pack() #place label widget into window
'''
#button
'''
topframe=Frame(app)
topframe.pack()

bottomframe=Frame(app)
bottomframe.pack(side=BOTTOM)

button1=Button(topframe, text="Button 1", fg="red") #fg color
button2=Button(topframe, text="Button 2", fg="blue") #fg color
button3=Button(topframe, text="Button 3", fg="green") #fg color
button4=Button(bottomframe, text="Button 4", fg="purple") #fg color

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
'''
#fill color
'''
one=Label(app, text="one", bg="red", fg="white")
one.pack()
two=Label(app, text="two", bg="green", fg="black")
two.pack(fill=X) #will grow in the x direction if window size changes
three=Label(app, text="three", bg="blue", fg="white")
three.pack(side=LEFT, fill=BOTH, expand=TRUE) #will grow in both direction if window size changes
'''

#grid
'''
label1=Label(app, text="name")
label2=Label(app, text="passwd")
entry1=Entry(app) #line input
entry2=Entry(app) #line input

label1.grid(row=0, sticky=E) #no more pack(), column defaults to zero, top
#grid sticky North East West South
label2.grid(row=1, sticky=E) #bottom

entry1.grid(row=0, column=1) #same row as label1
entry2.grid(row=1, column=1) #same row as label2

c=Checkbutton(app, text="keep me logged in") #little square check box
c.grid(columnspan=2) #take two columns
'''
#event buttonclick
'''
def printname(event):
	print("hello world!")

#button1=Button(app, text="printname", command=printname)
button1=Button(app, text="printname")
button1.bind("<Button-1>", printname) #binds button click to function with events
button1.pack()
'''
#event on frame
'''
def leftclick(event):
	print("left")

def middleclick(event):
	print("middle")

def rightclick(event):
	print("right")

frame=Frame(app, width=320, height=240)
frame.bind("<Button-1>", leftclick)
frame.bind("<Button-2>", middleclick)
frame.bind("<Button-3>", rightclick)

frame.pack()
'''


class mybuttons:
	def __init__(self, master): #master gui
		frame=Frame(master)
		frame.pack() #blank window
		self.printbutton=Button(frame, text="hello world!", command=self.printmessage)
		self.printbutton.pack(side=LEFT) #with a button
		self.quitbutton=Button(frame, text="bye", command=frame.quit) #frame.quit is built-in
		self.quitbutton.pack(side=LEFT) #will come out on right because theres printbutton already on the left

	def printmessage(self):
		print("hello, world!")

b=mybuttons(app) #app is now master













app.mainloop() #mainloop