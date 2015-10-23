from tkinter import *

def menu_new():
	lb.config(text="new called")
def menu_open():
	lb.config(text="open called")
def menu_about():
	lb.config(text="about called")
def menu_exit():
	app.destroy()
	
app=Tk()
app.title("example")

menubar=Menu(app)
app.config(menu=menubar)

filemenu=Menu(menubar)
menubar.add_cascade(label="file", menu=filemenu)
helpmenu=Menu(menubar)
menubar.add_cascade(label="help", menu=helpmenu)

filemenu.add_command(label="new", command=menu_new)
filemenu.add_command(label="open", command=menu_open)
filemenu.add_separator()
filemenu.add_command(label="exit", command=menu_exit)
helpmenu.add_command(label="about", command=menu_about)


lb=Label(app, text="hello, world!", width=50, height=3)
lb.pack()

app.mainloop()