#!/usr/bin/env python
import pygame
from socket import *
from threading import *



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


width=255
height=255
size=(width, height)
screen=pygame.display.set_mode(size)

pygame.display.set_caption("mygame")

done=False

clock=pygame.time.Clock() #for clock.tick(60)

fps=20


'''
game vars============================================================
'''

def clientRecv():
	while True:
		serverIndex=list(clientsocket.recv(1024))
		row=serverIndex[0]
		col=serverIndex[1]
		grid[row][col]=1
		
servername='127.0.0.1'
serverport=7000
clientsocket=socket(AF_INET, SOCK_STREAM)
clientsocket.connect((servername, serverport))
Thread(target=clientRecv).start()

gridwidth=20
gridheight=20
margin=5

grid=[]
for row in range(10):
	grid.append([])
	for col in range(10):
		grid[row].append(0)
		

		
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
			clientsocket.close()
			done=True
		if i.type == pygame.MOUSEBUTTONDOWN:
			pos=pygame.mouse.get_pos()
			col=pos[0]//(gridwidth+margin)
			row=pos[1]//(gridheight+margin)
			grid[row][col]=2 #client
			#send info to server
			clientindex=[row, col]
			indexbytes=bytes(clientindex)
			clientsocket.send(indexbytes)
			
			
	'''
game logic===========================================================
	'''	
	

	
	'''
draw loop============================================================
	'''

	for row in range(10):
		for col in range(10):
			color=white
			if grid[row][col]==1:
				color=green #server
			elif grid[row][col]==2:
				color=red #client
			pygame.draw.rect(screen, color, [(margin+gridwidth)*col+margin, (margin+gridheight)*row+margin, gridwidth, gridheight])
	

	
	'''
final render=========================================================
	'''
	
	pygame.display.flip() #update frame
	clock.tick(fps) #60fps
	
	screen.fill(black) #clear screen AFTER clock.tick wait

pygame.quit() #hangs on IDLE if it isnt here.

