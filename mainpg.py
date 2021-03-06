#!/usr/bin/env python
import pygame
import math
import random
pygame.init()

'''
4bytes 32bit hex: 0x0~0xffffffff(8) dec: 0~4294967295
2bytes 16bit hex: 0x0~0xffff(4) dec: 0~65535
1byte 8bit hex: 0x0~0xff(2) dec: 0~255
'''

black=(0x0, 0x0, 0x0)
white=(0xff, 0xff, 0xff)
red=(0xff, 0x0, 0x0)
green=(0x0, 0xff, 0x0)
blue=(0x0, 0x0, 0xff)
lightblue=(0x0, 0xbf, 0xff)

pi=3.141592653

width=700
height=500

size=(width, height)
screen=pygame.display.set_mode(size)

pygame.display.set_caption("mygame")

done=False

clock=pygame.time.Clock() #for clock.tick(60)

fps=60


'''
game vars============================================================
'''

class ball():
	x=0
	y=0
	change_x=0
	change_y=0
	size=10
	color=white
	
	def draw(self, screen):
		pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)
		
	def move(self):
		self.x+=self.change_x
		self.y+=self.change_y
		
	def bounce(self):
		if self.x > width-self.size or self.x < self.size:
			self.change_x*=-1
		if self.y > height-self.size or self.y < self.size:
			self.change_y*=-1
		
redball=ball()
blueball=ball()

redball.x=50
redball.y=50
blueball.x=600
blueball.y=400

redball.change_x=5
redball.change_y=5
blueball.change_x=-7
blueball.change_y=-7

redball.color=red
blueball.color=blue



'''
=====================================================================
'''

while not done:
	'''
event loop===========================================================
	'''
	
	pygame.event.pump()
	for i in pygame.event.get():
		if i.type == pygame.QUIT:	#close button
			done=True
	
	
			
	'''
game logic===========================================================
	'''	

	redball.move()
	blueball.move()
	
	redball.bounce()
	blueball.bounce()
	
	
	
	
	
	'''
draw loop============================================================
	'''

	
	redball.draw(screen)
	blueball.draw(screen)
	
	
	
	
	
	
	
	'''
final render=========================================================
	'''
	
	pygame.display.flip() #update frame
	clock.tick(fps) #60fps
	
	screen.fill(white) #clear screen AFTER clock.tick wait

pygame.quit() #hangs on IDLE if it isnt here.

