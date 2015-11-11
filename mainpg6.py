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
yellow=(0xff, 0xff, 0x99)

pi=3.141592653

width=800
height=600

size=(width, height)
screen=pygame.display.set_mode(size)

pygame.display.set_caption("어드벤처 이미지")

done=False

clock=pygame.time.Clock() #for clock.tick(60)

fps=60


'''
game vars============================================================
'''

pygame.mouse.set_visible(0)

atlas_image=pygame.image.load("terrain_atlas.png").convert()
def set_tile(tile_x, tile_y, tile_width, tile_height, x, y):
	atlas_image.set_colorkey(black)
	screen.blit(atlas_image, [x, y], [tile_x*32, tile_y*32, tile_width*32, tile_height*32])

def expand_tile(tile_x, tile_y, width, height):
	tile_x*=32
	tile_y*=32
	width*=32
	height*=32
	global image
	image=pygame.Surface([width, height])
	image.set_colorkey(black)
	#first row
	image.blit(atlas_image, [0,0], [tile_x, tile_y, 32, 32])
	for column in range(width//32-2):
		image.blit(atlas_image, [(column+1)*32, 0], [tile_x+32, tile_y, 32, 32])
	image.blit(atlas_image, [(width//32-1)*32, 0], [tile_x+64, tile_y, 32, 32])
	#middle rows
	for row in range(height//32-2):
		image.blit(atlas_image, [0, (row+1)*32], [tile_x, tile_y+32, 32, 32])
		for column in range(width//32-2):
			image.blit(atlas_image, [(column+1)*32, (row+1)*32], [tile_x+32, tile_y+32, 32, 32])
		image.blit(atlas_image, [(width//32-1)*32, (row+1)*32], [tile_x+64, tile_y+32, 32, 32])
	#last row
	image.blit(atlas_image, [0, (height//32-1)*32], [tile_x, tile_y+64, 32, 32])
	for column in range(width//32-2):
		image.blit(atlas_image, [(column+1)*32, (height//32-1)*32], [tile_x+32, tile_y+64, 32, 32])
	image.blit(atlas_image, [(width//32-1)*32, (height//32-1)*32], [tile_x+64, tile_y+64, 32, 32])
	
expand_tile(16, 23, 18, 0)

def set_expanded_tile(x, y):
	screen.blit(image, [x, y])


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
		
	
	
			
	'''
game logic===========================================================
	'''	

	
	
	
	
	
	
	'''
draw loop============================================================
	'''


	set_tile(30, 0, 2, 5, 100, 100) #tree 1
	set_tile(29, 28, 3, 4, 300, 250) #tree 2
	set_tile(16, 23, 3, 3, 150, 450) #brick wall
	set_expanded_tile(128, 320)
	
			
	'''
final render=========================================================
	'''
	
	pygame.display.flip() #update frame
	clock.tick(fps) #60fps
	
	screen.fill(yellow) #clear screen AFTER clock.tick wait

pygame.quit() #hangs on IDLE if it isnt here.

