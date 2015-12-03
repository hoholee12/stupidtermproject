#!/usr/bin/env python
import pygame
import pygame.gfxdraw
import math
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
back_color=[255, 255, 153]

pi=3.141592653


width=800
height=600
size=(width, height)
screen=pygame.display.set_mode(size)

pygame.display.set_caption("mygame")

done=False

clock=pygame.time.Clock() #for clock.tick(60)

fps=30


'''
game vars============================================================
'''

class GraphicWall(pygame.sprite.Sprite):
	def __init__(self):
		self.myimage=pygame.image.load("terrain_atlas.png").convert()
		self.image=pygame.Surface([width, height])


	def setGraphic(self, tilex, tiley, tilewidth, tileheight, x, y, width, height):		
		for row in range(height//tileheight):
			for col in range(width//tilewidth):
				self.image.blit(self.myimage,[col*tilewidth, row*tileheight], [tilex, tiley, tilewidth, tileheight])
				
		self.rect=self.image.get_rect()
		self.rect.y=y
		self.rect.x=x
		self.image.set_colorkey(black)
		
	def setGraphic2(self, tilex, tiley, x, y, width, height):
		self.image.blit(self.myimage, [0, 0], [tilex, tiley, 32, 32])
		for col in range(width//32-2):
			self.image.blit(self.myimage, [(col+1)*32, 0], [tilex+32, tiley, 32, 32])
			
		self.image.blit(self.myimage, [(width//32-1)*32, 0], [tilex+64, tiley, 32, 32])
		for row in range(height//32-2):
			self.image.blit(self.myimage, [0, (row+1)*32], [tilex, tiley+32, 32, 32])
			for col in range(width//32-2):
				self.image.blit(self.myimage, [(col+1)*32, (row+1)*32], [tilex+32, tiley+32, 32, 32])
			self.image.blit(self.myimage, [(width//32-1)*32, (row+1)*32], [tilex+64, tiley+32, 32, 32])
		
		self.image.blit(self.myimage, [0, (height//32-1)*32], [tilex, tiley+64, 32, 32])
		
		for col in range(width//32-2):
			self.image.blit(self.myimage, [(col+1)*32, (height//32-1)*32], [tilex+32, tiley+64, 32, 32])

		self.image.blit(self.myimage, [(width//32-1)*32, (height//32-1)*32], [tilex+64, tiley+64, 32, 32])
		self.rect=self.image.get_rect()
		self.rect.y=y
		self.rect.x=x
		self.image.set_colorkey(black)
		
class StoneWall(GraphicWall):
	def __init__(self, x, y, width, height):
		pygame.sprite.Sprite.__init__(self)
		tilex=32*16
		tiley=32*29
		self.setGraphic2(tilex, tiley, x, y, width, height)
		
class StoneWall2(GraphicWall):
	def __init__(self, x, y, width, height):
		pygame.sprite.Sprite.__init__(self)
		tilex=32*16
		tiley=32*23
		self.setGraphic2(tilex, tiley, x, y, width, height)
		
class Tree1(GraphicWall):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		width=64
		height=160
		tilewidth=64
		tileheight=160
		tilex=32*30
		tiley=32*0
		self.setGraphic(tilex, tiley, tilewidth, tileheight, x, y, width, height)
		
		
class Tree2(GraphicWall):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		width=96
		height=128*2
		tilewidth=96
		tileheight=128
		tilex=32*29
		tiley=32*28
		self.setGraphic(tilex, tiley, tilewidth, tileheight, x, y, width, height)
		
class WaterWall(GraphicWall):
	def __init__(self, x, y, width, height):
		pygame.sprite.Sprite.__init__(self)
		tilex=32*9
		tiley=32*11
		self.setGraphic2(tilex, tiley, x, y, width, height)
		
class GardenWall(GraphicWall):
	def __init__(self, x, y, width, height):
		pygame.sprite.Sprite.__init__(self)
		tilex=32*5
		tiley=32*17
		self.setGraphic2(tilex, tiley, x, y, width, height)
		
class TallGrass(GraphicWall):
	def __init__(self, x, y, width, height):
		pygame.sprite.Sprite.__init__(self)
		tilex=32*0
		tiley=32*22
		self.setGraphic2(tilex, tiley, x, y, width, height)

class FallGrass(GraphicWall):
	def __init__(self, x, y, width, height):
		pygame.sprite.Sprite.__init__(self)
		tilex=32*0
		tiley=32*28
		self.setGraphic2(tilex, tiley, x, y, width, height)

class Player(pygame.sprite.Sprite):
	change_x=0
	change_y=0
	frame=0
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.images=[]
		for i in range(1, 9):
			img=pygame.image.load("cat/cat"+str(i)+".png").convert()
			img.set_colorkey(white)
			self.images.append(img)
		self.image=self.images[0]
		self.rect=self.image.get_rect()
		
	def changespeed(self, x, y):
		self.change_x+=x
		self.change_y+=y
		
	def update(self, walls):
		old_x=self.rect.x
		new_x=old_x+self.change_x
		self.rect.x=new_x
		collide=pygame.sprite.spritecollide(self, walls, False)
		if collide:
			self.rect.x=old_x
		old_y=self.rect.y
		new_y=old_y+self.change_y
		self.rect.y=new_y
		collide=pygame.sprite.spritecollide(self, walls, False)
		if collide:
			self.rect.y=old_y
		#left
		if self.change_x<0:
			self.frame+=1
			if self.frame>3*4:
				self.frame=0
			self.image=self.images[self.frame//4]
		#right
		if self.change_x>0:
			self.frame+=1
			if self.frame>3*4:
				self.frame=0
			self.image=self.images[self.frame//4+4]
			
			
def setupRoomOne():
	wall_list=pygame.sprite.Group()
	wall=StoneWall(390, 80, 96, 448)
	wall_list.add(wall)
	wall=StoneWall2(600, 0, 128, 320)
	wall_list.add(wall)
	return wall_list
		
def setupRoomTwo():
	wall_list=pygame.sprite.Group()
	wall=Tree1(100, 100)
	wall_list.add(wall)
	wall=Tree1(300, 250)
	wall_list.add(wall)
	wall=TallGrass(100, 400, 64, 160)
	wall_list.add(wall)
	wall=Tree1(500, 160)
	wall_list.add(wall)
	wall=FallGrass(600, 128, 192, 160)
	wall_list.add(wall)
	wall=Tree1(700, 350)
	wall_list.add(wall)
	return wall_list
		
def setupRoomThree():
	wall_list=pygame.sprite.Group()
	
	wall=WaterWall(64, 64, 192, 192)
	wall_list.add(wall)
	wall=GardenWall(128, 325, 256, 192)
	wall_list.add(wall)
	wall=Tree1(520, 256)
	wall_list.add(wall)
	return wall_list
		
#end		
player=Player()
player.rect.x=50
player.rect.y=50
movingsprites=pygame.sprite.Group()
movingsprites.add(player)

current_room=1
wall_list=setupRoomOne()	

		
		
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
				player.changespeed(-5,0)
			if i.key == pygame.K_RIGHT:
				player.changespeed(5,0)
			if i.key == pygame.K_UP:
				player.changespeed(0,-5)
			if i.key == pygame.K_DOWN:
				player.changespeed(0,5)
				
		if i.type == pygame.KEYUP:
			if i.key == pygame.K_LEFT:
				player.changespeed(5,0)
			if i.key == pygame.K_RIGHT:
				player.changespeed(-5,0)
			if i.key == pygame.K_UP:
				player.changespeed(0,5)
			if i.key == pygame.K_DOWN:
				player.changespeed(0,-5)
				

				
				
				
				
				
				
				
	'''
game logic===========================================================
	'''	
	player.update(wall_list)
	
	if player.rect.x < -15:
		if current_room == 1:
			wall_list=setupRoomThree()
			current_room=3
			player.rect.x=790
		elif current_room ==3:
			wall_list=setupRoomTwo()
			player.rect.x=790
			current_room=2
		else:
			wall_list=setupRoomOne()
			player.rect.x=790
			current_room=1
			
	if player.rect.x > 801:
		if current_room == 1:
			wall_list=setupRoomTwo()
			current_room=2
			player.rect.x=0
		elif current_room == 2:
			wall_list=setupRoomThree()
			current_room=3
			player.rect.x=0
		else:
			wall_list=setupRoomOne()
			current_room=1
			player.rect.x=0
		
	if player.rect.y < -15:
		if current_room == 1:
			wall_list=setupRoomThree()
			current_room=3
			player.rect.y=590
		elif current_room ==3:
			wall_list=setupRoomTwo()
			player.rect.y=590
			current_room=2
		else:
			wall_list=setupRoomOne()
			player.rect.y=590
			current_room=1
			
	if player.rect.y > 601:
		if current_room == 1:
			wall_list=setupRoomTwo()
			current_room=2
			player.rect.y=0
		elif current_room == 2:
			wall_list=setupRoomThree()
			current_room=3
			player.rect.y=0
		else:
			wall_list=setupRoomOne()
			current_room=1
			player.rect.y=0
	
	
	
	
	'''
draw loop============================================================
	'''
	movingsprites.draw(screen)
	wall_list.draw(screen)
	

	
	'''
final render=========================================================
	'''
	
	pygame.display.flip() #update frame
	clock.tick(fps) #60fps
	
	screen.fill(back_color) #clear screen AFTER clock.tick wait

pygame.quit() #hangs on IDLE if it isnt here.

