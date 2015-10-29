#!/cygdrive/c/Python34/python.exe
import pygame
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

pi=3.141592653

size=(700, 500)
screen=pygame.display.set_mode(size)

pygame.display.set_caption("mygame")

done=False

clock=pygame.time.Clock() #for clock.tick(60)

while not done:
'''
event loop===========================================================
'''
	for i in pygame.event.get():
		if i.type == pygame.QUIT:	#close button
			done=True

			
			
			
			
'''
game logic===========================================================
'''	
	
	
	
	

	
	
	
	
'''
draw loop============================================================
'''








'''
final render=========================================================
'''
	screen.fill(white) #clear screen
	
	pygame.display.flip() #update frame
	clock.tick(60) #60fps

pygame.quit() #hangs on IDLE if it isnt here.





