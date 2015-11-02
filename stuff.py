#!/cygdrive/c/Python34/python.exe
import pygame
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

pi=3.141592653

size=(700, 500)
screen=pygame.display.set_mode(size)

pygame.display.set_caption("mygame")

done=False

clock=pygame.time.Clock() #for clock.tick(60)

fps=60


'''
game vars============================================================
'''

val=[0,0,0,0,0,0,0] #zxcvsdf
on=[0,0,0,0,0,0,0] #zxcvsdf
max=200



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
			
		elif i.type == pygame.KEYDOWN:
			#lower key
			if i.key == pygame.K_z:
				val[0]=max+10
			elif i.key == pygame.K_x:
				val[2]=max+10
			elif i.key == pygame.K_c:
				val[4]=max+10
			elif i.key == pygame.K_v:
				val[6]=max+10
				
				
			#upper key
			elif i.key == pygame.K_s:
				val[1]=max+10
			elif i.key == pygame.K_d:
				val[3]=max+10
			elif i.key == pygame.K_f:
				val[5]=max+10		
	
			
	'''
game logic===========================================================
	'''	
	
	
	for i in range(0, 7):
		if val[i] == max+10:
			on[i]=1
		else:
			on[i]=0
		if val[i] <= 0:
			continue
		val[i]-=10

		
	

	
	
	
	
	'''
draw loop============================================================
	'''

	#lower
	for i in range(0, 7):
		if i%2 == 0:
			pygame.draw.rect(screen, blue, [i*30,200-val[i],30,val[i]])
		else:
			pygame.draw.rect(screen, lightblue, [i*30,200-val[i],30,val[i]])
	

	
	
	'''
final render=========================================================
	'''
	
	pygame.display.flip() #update frame
	clock.tick(fps) #60fps
	
	screen.fill(white) #clear screen AFTER clock.tick wait

pygame.quit() #hangs on IDLE if it isnt here.

