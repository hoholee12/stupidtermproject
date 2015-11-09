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

def draw_stick_figure(screen, x, y):
	pygame.draw.ellipse(screen, black, [1+x, y, 10, 10], 0)
	pygame.draw.line(screen, black, [5+x, 17+y], [10+x, 27+y], 2)
	pygame.draw.line(screen, black, [5+x, 17+y], [x, 27+y], 2)
	pygame.draw.line(screen, red, [5+x, 17+y], [5+x, 7+y], 2)
	pygame.draw.line(screen, red, [5+x, 7+y], [9+x, 17+y], 2)
	pygame.draw.line(screen, red, [5+x, 7+y], [1+x, 17+y], 2)
	
x_speed=0
y_speed=0
	
x_coord=10
y_coord=10

prev_x=x_coord
prev_y=y_coord

pos=pygame.mouse.get_pos()
prev_mousex=pos[0]
prev_mousey=pos[1]
	
#hide cursor
pygame.mouse.set_visible(0)
	
#default font
font=pygame.font.Font(None, 25)
text=font.render("press q to quit.", True, black)



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
				
		if i.type == pygame.KEYDOWN:
			if i.key == pygame.K_LEFT:
				x_speed=-6
			if i.key == pygame.K_RIGHT:
				x_speed=6
			if i.key == pygame.K_UP:
				y_speed=-6
			if i.key == pygame.K_DOWN:
				y_speed=6
		
		if i.type == pygame.KEYUP:
			if i.key == pygame.K_LEFT:
				x_speed=0
			if i.key == pygame.K_RIGHT:
				x_speed=0
			if i.key == pygame.K_UP:
				y_speed=0
			if i.key == pygame.K_DOWN:
				y_speed=0
		
			if i.key == pygame.K_q: #close key
				done=True
		
		
	
	
			
	'''
game logic===========================================================
	'''	
	pos=pygame.mouse.get_pos()
	if prev_mousex != pos[0] or prev_mousey != pos[1]: #if mouse moved
		prev_mousex=pos[0]
		prev_mousey=pos[1]
		x_coord=pos[0]
		y_coord=pos[1]
		prev_x=x_coord
		prev_y=y_coord	
	else:
		pygame.mouse.set_pos([x_coord, y_coord]) #mouse follows key press
	
	if prev_x != x_coord or prev_y != y_coord: #if key pressed
		prev_x=x_coord
		prev_y=y_coord

	x_coord=x_coord+x_speed
	y_coord=y_coord+y_speed
	
	
	'''
draw loop============================================================
	'''

	
	screen.blit(text, [width-200, height-30])
	
	draw_stick_figure(screen, x_coord, y_coord)
	
	
			
	'''
final render=========================================================
	'''
	
	pygame.display.flip() #update frame
	clock.tick(fps) #60fps
	
	screen.fill(white) #clear screen AFTER clock.tick wait

pygame.quit() #hangs on IDLE if it isnt here.

