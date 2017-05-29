from block import Block
import pygame

class RegBlock(Block):
	def __init__(self, screen, mario_speed, start_x):
		super(RegBlock,self).__init__()
		self.x = start_x
		self.y = 245
		self.speed = mario_speed
		self.screen = screen
		self.image = pygame.image.load('./mario_pics/reg_block.png')
		self.image = pygame.transform.scale(self.image, (27, 27))
		self.should_move_left = False
		self.should_move_right = False
		self.power_up_remaining = 0