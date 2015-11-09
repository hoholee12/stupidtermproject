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



class keys:
	val=[0,0,0,0,0,0,0,0] #zsxdcfv shift
	on=[0,0,0,0,0,0,0,0] #zsxdcfv shift
	lock=[0,0,0,0,0,0,0,0]
	max=230
	speed=max/(fps/6)
	def draw(self, screen, loc=[0,0]):
		for i in range(0, 7):
			if i%2 == 0:
				try:
					pygame.gfxdraw.box(screen, pygame.Rect(loc[0]+i*30, loc[1]+self.max-self.val[i], 30, self.val[i]), (0x0, 0x0, 0xff, self.val[i]))
				except:
					print(self.val[i])
					exit(1)
				
			else:
				pygame.gfxdraw.box(screen, pygame.Rect(loc[0]+i*30, loc[1]+self.max-self.val[i], 30, self.val[i]), (0x0, 0xbf, 0xff, self.val[i]))
				
	def drawscratch(self, screen, loc=[0,0]):
		pygame.gfxdraw.box(screen, pygame.Rect(loc[0]-50, loc[1]+self.max-self.val[7], 50, self.val[7]), (0xff, 0x0, 0x0, self.val[7]))
		pygame.draw.ellipse(screen, gray, [loc[0]-50, loc[1]+self.max, 50, 30])
		if self.on[7] == 1:
			pygame.draw.ellipse(screen, red, [loc[0]-50+10, loc[1]+self.max+5, 50-20, 30-10])
		else:
			pygame.draw.ellipse(screen, lightblue, [loc[0]-50+10, loc[1]+self.max+5, 50-20, 30-10])
				
	def drawunder(self, screen, font, loc=[0,0]):
		loc[1]+=200 #hax
		for i in range(0, 7):
			if i%2 ==0:
				if self.on[i] == 1:
					pygame.draw.rect(screen, red, [loc[0]+i*30, loc[1]+50, 30, 50])
					text=font.render(str(self.on[i]), True, white)
					screen.blit(text, [loc[0]+i*30, loc[1]+50])
				else:
					pygame.draw.rect(screen, gray, [loc[0]+i*30, loc[1]+50, 30, 50])
					text=font.render(str(self.on[i]), True, black)
					screen.blit(text, [loc[0]+i*30, loc[1]+50])
			else:
				if self.on[i] == 1:
					pygame.draw.rect(screen, red, [loc[0]+i*30, loc[1]+30, 30, 50])
					text=font.render(str(self.on[i]), True, white)
					screen.blit(text, [loc[0]+i*30, loc[1]+30])
				else:
					pygame.draw.rect(screen, gray, [loc[0]+i*30, loc[1]+30, 30, 50])
					text=font.render(str(self.on[i]), True, black)
					screen.blit(text, [loc[0]+i*30, loc[1]+30])
					
		pygame.draw.rect(screen, red, [loc[0], loc[1]+30, 210, 0])
		for i in range(0, 8):
			pygame.draw.rect(screen, black, [loc[0]+i*30, 0, 0, loc[1]+30])
				
	def logic(self):		
		for i in range(0, 8):
			if self.val[i] == self.max+self.speed:
				self.on[i]=1
			else:
				self.on[i]=0
			if self.val[i] <= 0:
				continue
			if self.lock[i] == 0:
				self.val[i]-=self.speed

		

mykeys=keys()

#default font
font=pygame.font.Font(None, 25)

		
		
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
			#lower key
			if i.key == pygame.K_z:
				mykeys.val[0]=mykeys.max+mykeys.speed
				mykeys.lock[0]=1
			if i.key == pygame.K_x:
				mykeys.val[2]=mykeys.max+mykeys.speed
				mykeys.lock[2]=1
			if i.key == pygame.K_c:
				mykeys.val[4]=mykeys.max+mykeys.speed
				mykeys.lock[4]=1
			if i.key == pygame.K_v:
				mykeys.val[6]=mykeys.max+mykeys.speed
				mykeys.lock[6]=1
			
				
				
			#upper key
			if i.key == pygame.K_s:
				mykeys.val[1]=mykeys.max+mykeys.speed
				mykeys.lock[1]=1
			if i.key == pygame.K_d:
				mykeys.val[3]=mykeys.max+mykeys.speed
				mykeys.lock[3]=1
			if i.key == pygame.K_f:
				mykeys.val[5]=mykeys.max+mykeys.speed
				mykeys.lock[5]=1
			
			#shift key
			if i.key == pygame.K_LSHIFT:
				mykeys.val[7]=mykeys.max+mykeys.speed
				mykeys.lock[7]=1
				
		if i.type == pygame.KEYUP:
			#lower key
			if i.key == pygame.K_z:
				mykeys.lock[0]=0
			if i.key == pygame.K_x:
				mykeys.lock[2]=0
			if i.key == pygame.K_c:
				mykeys.lock[4]=0
			if i.key == pygame.K_v:
				mykeys.lock[6]=0
			
				
				
			#upper key
			if i.key == pygame.K_s:
				mykeys.lock[1]=0
			if i.key == pygame.K_d:
				mykeys.lock[3]=0
			if i.key == pygame.K_f:
				mykeys.lock[5]=0
				
			#shift key
			if i.key == pygame.K_LSHIFT:
				mykeys.lock[7]=0
	
			
	'''
game logic===========================================================
	'''	
	
	
		
	mykeys.logic()

	
	
	
	
	'''
draw loop============================================================
	'''

	
	mykeys.draw(screen, [50, 150])
	mykeys.drawunder(screen, font, [50, 150])
	mykeys.drawscratch(screen, [50, 150])
	
	for i in range(0, 7):
		text=font.render(str(mykeys.on[i]), True, black)
		screen.blit(text, [width-200+25*i, height-30])
	
	
	'''
final render=========================================================
	'''
	
	pygame.display.flip() #update frame
	clock.tick(fps) #60fps
	
	screen.fill(white) #clear screen AFTER clock.tick wait

pygame.quit() #hangs on IDLE if it isnt here.

