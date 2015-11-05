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

star_list=[]

for i in range(50):
	x=random.randrange(0, width)
	y=random.randrange(0, height)
	star_list.append([x, y])


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


	
	
	
	'''
draw loop============================================================
	'''

	for i in range(len(star_list)):
		pygame.draw.circle(screen, blue, star_list[i], 2)
		star_list[i][1]+=1
		star_list[i][0]+=1
		
		if star_list[i][1]>height:
			x=random.randrange(0, width)
			star_list[i][0]=x
			y=random.randrange(-50, -10)
			star_list[i][1]=y
		if star_list[i][0]>width:
			x=random.randrange(-50, -10)
			star_list[i][0]=x
			y=random.randrange(0, height)
			star_list[i][1]=y
			
	'''
final render=========================================================
	'''
	
	pygame.display.flip() #update frame
	clock.tick(fps) #60fps
	
	screen.fill(white) #clear screen AFTER clock.tick wait

pygame.quit() #hangs on IDLE if it isnt here.

