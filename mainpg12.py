#!/usr/bin/env python
import pygame
import time
import sys
import random

screen_width=400
screen_height=640
white=[255, 255, 255]
yellow=[255, 255, 0]
left_click=1
block_size=56
block_margin_x=1
block_margin_y=152
block_padding_x=1
block_padding_y=0
skip_rate=5

class block():
	val="void"
	top=None
	bottom=None
	left=None
	right=None
	coord_x=0
	coord_y=0
	visible=True

	def __init__(self, x, y, val):
		self.val=val
		self.coord_x=block_margin_x+(x*(block_size+block_padding_x))
		self.coord_y=block_margin_y+(y*(block_size+block_padding_y))

	def dropdown(self):
		if(self.top is not None) and(self.val=="void") and(self.top.val!="void"):
			self.val=self.top.val
			self.top.val="void"
			return True
		else:
			return False

	def samecolor(self):
		count=1
		self.visible=False
		if(self.left is not None) and(self.left.visible) and(self.val==self.left.val):
			count+=self.left.samecolor()
		if(self.right is not None) and(self.right.visible) and (self.val == self.right.val):
			count+=self.right.samecolor()
		if(self.top is not None) and(self.top.visible) and (self.val == self.top.val):
			count+=self.top.samecolor()
		if(self.bottom is not None) and(self.bottom.visible) and (self.val == self.bottom.val):
			count+=self.bottom.samecolor()
		return count

	def getimage(self):
		if self.val == "red":
			return pygame.image.load('candy_red.png').convert_alpha()
		elif self.val == "blue":
			return pygame.image.load('candy_blue.png').convert_alpha()
		elif self.val == "yellow":
			return pygame.image.load('candy_yellow.png').convert_alpha()
		elif self.val == "green":
			return pygame.image.load('candy_green.png').convert_alpha()
		elif self.val == "purple":
			return pygame.image.load('candy_purple.png').convert_alpha()

	def draw(self, screen):
		if self.val != "void":
			screen.blit(self.getimage(), [self.coord_x, self.coord_y])


class world():
	mat=[]
	skip_rate=0
	score=0

	def __init__(self, screen):
		self.screen=screen
		self.creategrid()
		self.fillblock()

		for x in range(7):
			for y in range(7):
				if x>0:
					self.mat[x][y].left=self.mat[x-1][y]
				if x<6:
					self.mat[x][y].left=self.mat[x+1][y]
				if y>0:
					self.mat[x][y].left=self.mat[x][y-1]
				if y<6:
					self.mat[x][y].left=self.mat[x][y+1]

	def creategrid(self):
		for x in range(7):
			sublist=[]
			self.mat.append(sublist)
			for y in range(7):
				sublist.append(block(x, y, "void"))

	def fillblock(self):
		for x in range(7):
			for y in range(7):
				if(self.mat[x][y].val == "void"):
					self.mat[x][y].val=self.randomcolor()
		return True

	def randomcolor(self):
		random.random()
		i=random.randrange(0, 5)
		if i== 0:
			return "red"
		elif i==1:
			return "blue"
		elif i==2:
			return "yellow"
		elif i==3:
			return "green"
		elif i==4:
			return "purple"

	def draw(self):
		self.screen.fill(white)
		background=pygame.image.load('background.png').convert()
		self.screen.blit(background, [0, 0])
		for x in range(7):
			for y in range(7):
				self.mat[x][y].draw(self.screen)

		font=pygame.font.Font(None, 35)
		text=font.render(str(self.score), True, yellow)
		self.screen.blit(text, [230, 108])

		pygame.display.update()

	def blockselect(self, x, y):
		coord_x=int((x-block_margin_x)/(block_size+block_padding_x))
		coord_y=int((y-block_margin_y)/(block_size+block_padding_y))
		if(coord_x>=0 and coord_x<7) and (coord_y>=0 and coord_y<7):
			count=self.mat[coord_x][coord_y].samecolor()
		if count>2:
			self.score+=count
			for i in range(7):
				for j in range(7):
					if self.mat[i][j].visible==False:
						self.mat[i][j].val="void"
						self.mat[i][j].visible=True
			return True
		else:
			for i in range(7):
				for j in range(7):
					if self.mat[i][j].visible==False:
						self.mat[i][j].visible=True
			return False
				
	def blockdropdown(self):
		if self.skip_rate<skip_rate:
			self.skip_rate+=1
			return False
		else:
			self.skip_rate=0
			count=0
			for i in range(7):
				for j in range(7):
					if self.mat[i][6-j].dropdown():
						count+=1
						
			if count>0:
				return False
			else:
				self.fillblock()
				return True
				
pygame.init()
size=[screen_width, screen_height]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("candy pang")
theworld=world(screen)
done=False
dropdownflag=False

clock=pygame.time.Clock()

while done==False:
	pos=pygame.mouse.get_pos()
	x=pos[0]
	y=pos[1]
	
	for event in pygame.event.get():
		if event.type ==pygame.QUIT:
			done=True
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == left_click:
			if dropdownflag==False:
				if theworld.blockselect(x,y):
					dropdownflag=True
					
	if dropdownflag==True:
		if theworld.blockdropdown():
			dropdownflag=False
			
	theworld.draw()
	pygame.display.flip()
	clock.tick(30)
	
pygame.quit()