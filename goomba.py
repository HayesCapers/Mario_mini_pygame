import pygame
from pygame.sprite import Sprite
from physics import Physics

class Goomba(Sprite):
	def __init__(self, screen):
		super(Goomba, self).__init__()
		#/////////////////
		#/////IMAGES/////
		#///////////////
		self.goomba_load_1 = pygame.image.load('./mario_pics/goomba_move_1.png')
		self.goomba_1 = pygame.transform.scale(self.goomba_load_1, (30, 30))
		self.goomba_load_2 = pygame.image.load('./mario_pics/goomba_move_2.png')
		self.goomba_2 = pygame.transform.scale(self.goomba_load_2, (30, 30))
		self.goomba_dead_load = pygame.image.load('./mario_pics/goomba_smush.png')
		self.goomba_dead = pygame.transform.scale(self.goomba_dead_load, (30,30))


		#/////////////////
		#///ATTRIBUTES///
		#///////////////
		self.x = 620
		self.y = 303
		self.screen = screen
		self.speed = 2
		self.image_timer = 0
		self.dead = False

	def draw_goomba(self, mario, physics, background):
		self.image_timer += 1
		if self.image_timer >= 20:
			self.image_timer = 0
		self.goomba_move(mario)
		self.goomba_fall(background, mario, physics)
		if self.dead == False:
			self.screen.blit(self.goomba_img_selector(self.image_timer), [self.x, self.y])
		elif self.dead:
			self.screen.blit(self.goomba_dead, [self.x, self.y])

	
	def goomba_img_selector(self, timer):
		if (timer >= 0) and (timer < 10):
			return self.goomba_1
		elif (timer >= 10) and (timer <= 20):
			return self.goomba_2

	def goomba_move(self, mario):
		# self.y += physics.gravity
		if mario.should_move_right:
			self.speed = mario.speed + 2
		elif mario.should_move_left:
			self.speed = mario.speed - 6
		else:
			self.speed = 2
		self.x -= self.speed

	def goomba_fall(self, background, mario, physics):
		for i in background.holes:
			if self.x < 600:
				if self.x < (background.x - background.holes[i][1] + mario.x) and self.x >= background.x - background.holes[i][0] + mario.x:
					self.y += physics.gravity


	# def goomba_image_selector(self)





