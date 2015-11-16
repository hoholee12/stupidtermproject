#!/usr/bin/env python
import pygame
import pygame.gfxdraw
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
gray=(0x80, 0x80, 0x80)
orange=(0xff, 0xa5, 0x0)

pi=3.141592653


width=700
height=400
size=(width, height)
screen=pygame.display.set_mode(size)

pygame.display.set_caption("mygame")

done=False

clock=pygame.time.Clock() #for clock.tick(60)

fps=60


'''
game vars============================================================
'''

class Block(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface([width, height])
		self.image.fill(color)
		self.rect=self.image.get_rect()
		
	def reset_pos(self):
		self.rect.y=random.randrange(-100, -10)
		self.rect.x=random.randrange(0, width)
		
	def update(self, change_y):
		self.rect.y+=change_y
		if self.rect.y>height:
			self.reset_pos()
		
		
block_list=pygame.sprite.Group()
all_sprites_list=pygame.sprite.Group()

for i in range(50):
	block=Block(black, 20, 15)
	block.rect.x=random.randrange(width)
	block.rect.y=random.randrange(height)
	block_list.add(block)
	all_sprites_list.add(block)
	
player=Block(red, 20, 15)
all_sprites_list.add(player)

score=0
level=1
		
font=pygame.font.Font("nanumgothicBold.ttf", 25)
		
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
	
	pos=pygame.mouse.get_pos()
	player.rect.x=pos[0]
	player.rect.y=pos[1]
	
	blocks_hit_list=pygame.sprite.spritecollide(player, block_list, True)
	
	if len(blocks_hit_list)>0:
		score+=len(blocks_hit_list)
		
	if len(block_list) == 0:
		level+=1
		for i in range(level*10):
			block=Block(black, 20, 15)
			block.rect.x=random.randrange(width)
			block.rect.y=random.randrange(height)
			block_list.add(block)
			all_sprites_list.add(block)
	
	block_list.update(level)
	
	'''
draw loop============================================================
	'''


	all_sprites_list.draw(screen)
	text=font.render("점수: "+str(score), True, black)
	screen.blit(text, [10, 10])
	text=font.render("레벨: "+str(level), True, black)
	screen.blit(text, [10, 40])
	
	
	
	'''
final render=========================================================
	'''
	
	pygame.display.flip() #update frame
	clock.tick(fps) #60fps
	
	screen.fill(white) #clear screen AFTER clock.tick wait

pygame.quit() #hangs on IDLE if it isnt here.

