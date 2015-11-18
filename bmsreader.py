#!/usr/bin/env python
import pygame.mixer
import pygame

mixer=pygame.mixer
mixer.init()

class reader:
	WAV={}
	NUM=[]
	def __init__(self, filename):
		bms=open(filename, 'r')
		for i in bms.read().split('\n'):
			if i[:1] == '#':
				if i[1:4] == "WAV":
					try:
						self.WAV[i[4:6]]=mixer.Sound(filename.split('/')[0]+'/'+i.split(' ')[1])
					except pygame.error:
						self.WAV[i[4:6]]=mixer.Sound(filename.split('/')[0]+'/'+i.split(' ')[1].split('.')[0]+".ogg")
						
				if i[1:4] == "BPM":
					self.BPM=int(i.split(' ')[1])
					
					
				try:
					if int(i[1:4]):
						self.NUM.append(i.split(':')[0])
				except:
					pass
		#read everything here first, then close file
		
		
		
	def readnote(self):
		print(self.BPM)
		print(self.NUM)
		#busy=self.WAV["01"].play()
		#while busy.get_busy():
		#	pygame.time.delay(100)
			
hello=reader("bms/The Beauty Of Silence/The Beauty Of Silence(1 H).bms")
hello.readnote()








