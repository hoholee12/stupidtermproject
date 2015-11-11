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

pygame.mouse.set_visible(0)


background_position=[0,0]
background_image=pygame.image.load("saturn_family1.jpg").convert()
player_image=pygame.image.load("player.png").convert()
player_image.set_colorkey(white)


click_sound=pygame.mixer.Sound("click.wav")



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
			pass
		
		if i.type == pygame.KEYUP:
			pass
		
		
		
			if i.key == pygame.K_q: #close key
				done=True
		
		if i.type == pygame.MOUSEBUTTONDOWN:
			click_sound.play()
	
	
			
	'''
game logic===========================================================
	'''	

	
	
	
	
	
	
	'''
draw loop============================================================
	'''


	screen.blit(background_image, background_position)
	player_position=pygame.mouse.get_pos()
	screen.blit(player_image, player_position)
	
	
			
	'''
final render=========================================================
	'''
	
	pygame.display.flip() #update frame
	clock.tick(fps) #60fps
	
	screen.fill(white) #clear screen AFTER clock.tick wait

pygame.quit() #hangs on IDLE if it isnt here.

