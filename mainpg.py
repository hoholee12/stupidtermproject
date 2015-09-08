#!/cygdrive/c/Python34/python.exe
import pygame

pygame.init()

#assign them as tuple
white=(255, 255, 255)
black=(0, 0, 0)
red=(255, 0, 0) #optional parameter alpha(transparency, opaque)

clock=pygame.time.Clock() #returns clock object


game_display=pygame.display.set_mode((640, 480)) #need to return one tuple, not two function parameters!
pygame.display.set_caption('slither') #title for pygame top bar
#pygame.display.flip() #update entire screen, almost never used xDD

#pygame.display.update() #no parameters == flip() #not needed for now

#my game code here!

lead_x=300
lead_y=300
lead_x_change=0
lead_y_change=0


game_exit=0
while not game_exit:
	for event in pygame.event.get():
		#print(event)
		if event.type == pygame.QUIT:
			game_exit=1
		if event.type == pygame.KEYDOWN: #key pressed
			if event.key == pygame.K_LEFT:
				#lead_x-=10
				lead_x_change=-1
			if event.key == pygame.K_RIGHT:
				#lead_x+=10
				lead_x_change=1
			if event.key == pygame.K_UP:
				#lead_y-=10
				lead_y_change=-1
			if event.key == pygame.K_DOWN:
				#lead_y+=10
				lead_y_change=1
				
		if event.type == pygame.KEYUP: #key released
			lead_x_change=0
			lead_y_change=0
		
	
	lead_x+=lead_x_change
	lead_y+=lead_y_change

	game_display.fill(white)
	
	#pygame.draw.rect(game_display, black, [320, 240, 10, 100]) #where to draw, what color, x y width height as list
	#or
	game_display.fill(red, rect=[lead_x, lead_y, 10, 10]) #this is much faster! gpu rendering
	
	pygame.display.update()

	clock.tick(60) #60 fps







pygame.quit() #uninitialize pygame module

quit() #exit python