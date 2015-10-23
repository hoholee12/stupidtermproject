import threading

class mythread(threading.Thread):
	m=0
	n=0
	def __init__(self, s, e=5):
		threading.Thread.__init__(self)
		self.m=s
		self.n=e
		
	#override
	def run(self):
		for i in range(self.m, self.n):
			print(" %d"%i)
			
th=mythread(2)
th.start()

print("main print")

for i in range(100, 106):
	print(" %d"%i)
	
mythread(30, 35).start()

add=lambda x, y: x+y
print("hello", add(100, 200))