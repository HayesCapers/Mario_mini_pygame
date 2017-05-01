import pygame
import sys
from random import randint
def check_events(the_background, mario, screen):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:	
			if event.key == 273:
				mario.should_move('up', True)
			elif event.key == 276:
				mario.should_move('left', True)
				the_background.should_move('left', True)
				# blocks.should_move('left', True)
			elif event.key == 275:
				mario.should_move('right', True)
				the_background.should_move('right', True)
				# blocks.should_move('right', True)
		elif event.type == pygame.KEYUP:
			if event.key == 273:
				mario.should_move('up', False)
			if event.key == 276:
				mario.should_move('left', False)
				the_background.should_move('left', False)
				# blocks.should_move('left', False)
			if event.key == 275:
				mario.should_move('right', False)
				the_background.should_move('right', False)	
				# blocks.should_move('right', False)	


# def collision_detect(player, block):



	


