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

pi=3.141592653

size=(700, 500)
screen=pygame.display.set_mode(size)

pygame.display.set_caption("mygame")

done=False

clock=pygame.time.Clock() #for clock.tick(60)

fps=60

while not done:
	'''
event loop===============================================cccccc============
	'''
	for i in pygame.event.get():
		if i.type == pygame.QUIT:	#close button
			done=True
		elif i.type == pygame.KEYDOWN:
			True
		elif i.type == pygame.KEYUP:
			True
		elif i.type == pygame.MOUSEBUTTONDOWN:
			True
			
			
			
	'''
game logic===========================================================
	'''	
	
	
	
	

	
	
	
	
	'''
draw loop============================================================
	'''

	
	
	
	pygame.draw.line(screen, green, [0,0],[100,100], 5)
	pygame.draw.rect(screen, red, [100, 100, 320, 240])
	pygame.draw.ellipse(screen, blue, [100, 100, 320, 240])

	
	
	
	#draw multiple line
	for y_offset in range(0, 100, 10):
		pygame.draw.line(screen, red, [0, 10+y_offset], [100, 110+y_offset], 5) #[x, y] at the end, another [x, y] at the other end
	
	
	
	#draw sin, cos
	for i in range(200):
		radians_x=i/20
		radians_y=i/6
		x=int(75*math.sin(radians_x))+200
		y=int(75*math.cos(radians_y))+200
		pygame.draw.line(screen, black, [x, y], [x+5, y], 5)
	
	
	#draw x mark
	for x_offset in range(30, 300, 30):
		pygame.draw.line(screen,black,[x_offset,100],[x_offset-10,90],2)
		pygame.draw.line(screen,black,[x_offset,90],[x_offset-10,100],2)
		
		
		
	pygame.draw.rect(screen, black, [0,0, 250, 200], 2)
	pygame.draw.arc(screen, green, [0,0,250,200],  pi/2,     pi, 2) #90 -> 180
	pygame.draw.arc(screen, black, [0,0,250,200],     0,   pi/2, 2) #0 -> 90
	pygame.draw.arc(screen, red,   [0,0,250,200],3*pi/2,   2*pi, 2) #270 -> 360
	pygame.draw.arc(screen, blue,  [0,0,250,200],    pi, 3*pi/2, 2) #180 -> 270
		
		
	pygame.draw.polygon(screen, black, [[100, 100], [0, 200], [200, 200]], 5) #draw triangle(polygon)

	
	#draw text
	font=pygame.font.Font('nanumgothic.ttf', 25)
	
	text=font.render("hello!", True, black)
	screen.blit(text, [300, 300])
	text=font.render("안녕!", True, black)
	screen.blit(text, [400, 300])
	
	
	
	'''
final render=========================================================
	'''
	
	pygame.display.flip() #update frame
	clock.tick(fps) #60fps
	
	screen.fill(white) #clear screen AFTER clock.tick wait

pygame.quit() #hangs on IDLE if it isnt here.

