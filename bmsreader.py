#!/usr/bin/env python
import pygame.mixer
import pygame

mixer=pygame.mixer
mixer.init()

class reader:
	WAV={}
	NUM=[]
	BPM=None
	PLAY=[[0 for i in range(9)] for i in range(1024)]
	loop=-1
	bms=None
	filename=None
	def __init__(self, filename):
		self.filename=filename
		self.bms=open(self.filename, 'r')
		for i in self.bms.read().split('\n'):
			if i[:1] == '#':
				if i[1:4] == "WAV":
					try:
						self.WAV[i[4:6]]=mixer.Sound(self.filename.rsplit('/', 1)[0]+'/'+i.split(' ')[1])
					except pygame.error:
						self.WAV[i[4:6]]=mixer.Sound(self.filename.rsplit('/', 1)[0]+'/'+i.split(' ')[1].split('.')[0]+".ogg")
						
				if i[1:4] == "BPM":
					self.BPM=int(i.split(' ')[1])
					
					
				try:
					if int(i[1:4]):
						self.NUM.append(i.split(':')[0])
				except:
					pass
		#read everything here first, then close file
		
		
		
	def readnote(self):
		diff=None
		self.bms.seek(0)
		for i in self.bms.read().split('\n'):
			if i[:1] == '#':
				if i[1:4].isnumeric():
					if i[1:4] != diff:
						diff=i[1:4]
						self.loop+=1
						print(self.loop, diff)
						
					if i[4:6] == "01": #autoplay
						self.PLAY[self.loop][0]=i[7:]
						print("0:"+str(len(self.PLAY[self.loop][0])))
					elif i[4:6] == "11": #whitekey 1
						self.PLAY[self.loop][1]=i[7:]
						print("1:"+str(len(self.PLAY[self.loop][1])))
					elif i[4:6] == "12": #bluekey 1
						self.PLAY[self.loop][2]=i[7:]
						print("2:"+str(len(self.PLAY[self.loop][2])))
					elif i[4:6] == "13": #whitekey 2
						self.PLAY[self.loop][3]=i[7:]
						print("3:"+str(len(self.PLAY[self.loop][3])))
					elif i[4:6] == "14": #bluekey 2
						self.PLAY[self.loop][4]=i[7:]
						print("4:"+str(len(self.PLAY[self.loop][4])))
					elif i[4:6] == "15": #whitekey 3
						self.PLAY[self.loop][5]=i[7:]
						print("5:"+str(len(self.PLAY[self.loop][5])))
					elif i[4:6] == "18": #bluekey 3
						self.PLAY[self.loop][6]=i[7:]
						print("6:"+str(len(self.PLAY[self.loop][6])))
					elif i[4:6] == "19": #whitekey 4
						self.PLAY[self.loop][7]=i[7:]
						print("7:"+str(len(self.PLAY[self.loop][7])))
					elif i[4:6] == "16": #scratch
						self.PLAY[self.loop][8]=i[7:]
						print("8:"+str(len(self.PLAY[self.loop][8])))
						
		print(self.loop, diff)
						
						
						
	def playnote(self):
		j=0
		for i in range(0, self.loop):
			for k in range(0, len(str(self.PLAY[i][j])), 2):
				for j in range(0, 9):
					print(str(j)+":"+str(len(str(self.PLAY[i][j]))))

					if str(self.PLAY[i][j])[k:k+2] == "00" or str(self.PLAY[i][j])[k:k+2] == "0" or str(self.PLAY[i][j])[k:k+2] == "":
						pass
					else:
						print("osim:"+str(self.PLAY[i][j])[k:k+2])
						self.WAV[str(self.PLAY[i][j])[k:k+2]].play()
				pygame.time.delay(100) #140bpm

						
				'''	
					if i[4:6] == "01": #autoplay
						for j in range(1, len(i)-7, 2):
							print(i[j+6:j+8])
							if i[j+6:j+8] == "00":
								pygame.time.delay(1)
								continue
							busy=self.WAV[i[j+6: j+8]].play()
							pygame.time.delay(1)
					if i[4:6] == "11": #whitekey 1
						for j in range(1, len(i)-7, 2):
							print(i[j+6:j+8])
							if i[j+6:j+8] == "00":
								pygame.time.delay(1)
								continue
							busy=self.WAV[i[j+6: j+8]].play()
							pygame.time.delay(1)
					if i[4:6] == "12": #bluekey 1
						for j in range(1, len(i)-7, 2):
							print(i[j+6:j+8])
							if i[j+6:j+8] == "00":
								pygame.time.delay(1)
								continue
							busy=self.WAV[i[j+6: j+8]].play()
							pygame.time.delay(1)
					if i[4:6] == "13": #whitekey 2
						for j in range(1, len(i)-7, 2):
							print(i[j+6:j+8])
							if i[j+6:j+8] == "00":
								pygame.time.delay(1)
								continue
							busy=self.WAV[i[j+6: j+8]].play()
							pygame.time.delay(1)
					if i[4:6] == "14": #bluekey 2
						for j in range(1, len(i)-7, 2):
							print(i[j+6:j+8])
							if i[j+6:j+8] == "00":
								pygame.time.delay(1)
								continue
							busy=self.WAV[i[j+6: j+8]].play()
							pygame.time.delay(1)
					if i[4:6] == "15": #whitekey 3
						for j in range(1, len(i)-7, 2):
							print(i[j+6:j+8])
							if i[j+6:j+8] == "00":
								pygame.time.delay(1)
								continue
							busy=self.WAV[i[j+6: j+8]].play()
							pygame.time.delay(1)
					if i[4:6] == "18": #bluekey 3
						for j in range(1, len(i)-7, 2):
							print(i[j+6:j+8])
							if i[j+6:j+8] == "00":
								pygame.time.delay(1)
								continue
							busy=self.WAV[i[j+6: j+8]].play()
							pygame.time.delay(1)
					if i[4:6] == "19": #whitekey 4
						for j in range(1, len(i)-7, 2):
							print(i[j+6:j+8])
							if i[j+6:j+8] == "00":
								pygame.time.delay(1)
								continue
							busy=self.WAV[i[j+6: j+8]].play()
							pygame.time.delay(1)
							
		
		
		print(self.BPM)
		print(self.NUM)
		busy=self.WAV["01"].play()
		while busy.get_busy():
			pygame.time.delay(100)
			'''
			
hello=reader("bms/The Beauty Of Silence/The Beauty Of Silence(1 H).bms")
hello.readnote()
hello.playnote()








