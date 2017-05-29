from pygame.sprite import Sprite
# from question_block import QuestionBlock

class Block(Sprite):
	def __init__(self):
		super (Block,self).__init__()

	def draw_block(self, background):
		if background.should_move_left:
			self.x += self.speed
		elif background.should_move_right:
			self.x -= self.speed
		self.screen.blit(self.image, [self.x,self.y])	