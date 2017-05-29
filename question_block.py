import pygame
from pygame.sprite import Sprite
from block import Block

class QuestionBlock(Block):
	def __init__(self, screen, mario_speed, start_x):
		super(QuestionBlock,self).__init__()
		self.x = start_x
		self.y = 245
		self.speed = mario_speed
		self.screen = screen
		self.image = pygame.image.load('./mario_pics/question_block.png')
		self.image = pygame.transform.scale(self.image, (27, 27))
		self.should_move_left = False
		self.should_move_right = False
		self.power_up_remaining = 1

	
		
	# def should_move(self, direction, true_or_false):
	# 	if direction == 'up':
	# 		self.should_move_up = true_or_false
	# 	if direction == 'right':
	# 		self.should_move_right = true_or_false
	# 	elif direction == 'left':
	# 		self.should_move_left = true_or_false

	# def update_x(self, background):
	# 	self.x = background.x - self.x
	# 	return self.x