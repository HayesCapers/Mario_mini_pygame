import pygame 
from pygame.sprite import Sprite

class Star(Sprite):
	def __init__(self, screen, start_x):
		super(Star,self).__init__()
		self.image_1_load = pygame.image.load('./mario_pics/star_1.png')
		self.image_1 = pygame.transform.scale(self.image_1_load, (27,27))
		self.image_2_load = pygame.image.load('./mario_pics/star_2.png')
		self.image_2 = pygame.transform.scale(self.image_2_load, (27,27))
		self.x = start_x
		self.y = 245
		self.max_height = 200
		self.speed = 2
		self.screen = screen
		self.image_timer = 0
		self.move_timer = 0

	def draw_me(self, background, physics, block_group, mario):
		self.move_timer += 1
		self.image_timer += 1
		self.adjust_powerup_speed(mario)
		if self.image_timer >= 14:
			self.image_timer = 0
		if self.move_timer <= 20:
			self.y -= self.speed
		elif self.move_timer > 20 and self.y < background.floor + 14:
			self.y += physics.gravity
		if self.move_timer > 10:
			self.x -= self.speed
		# self.dont_go_through_blocks(block_group)
		self.screen.blit(self.star_img_selector(self.image_timer), [self.x, self.y])

	def star_img_selector(self, timer):
		if (timer >= 0) and (timer < 7):
			return self.image_1
		elif (timer >= 7) and (timer <= 14):
			return self.image_2

	def adjust_powerup_speed(self,mario):
		if mario.should_move_right:
			self.speed = mario.speed + 2
		elif mario.should_move_left:
			self.speed = mario.speed - 6
		else:
			self.speed = 2

	# def dont_go_through_blocks(self,block_group):
	# 	for block in block_group:
	# 		if self.x <= block.x and self.x >= block.x - 27:
	# 			if self.y <= block.y - 34 and self.y > block.y - 41:
	# 					self.y = block.y - 10
					
						

	
