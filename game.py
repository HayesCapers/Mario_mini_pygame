import pygame
import sys
from random import randint
from game_functions import check_events
from background import Background
from mario import Mario
from physics import Physics
from goomba import Goomba
from block import Block
from pygame.sprite import Group
from power_up import Star
from math import fabs


def run_game():
	pygame.init()


	screen_size = (600, 385)
	screen = pygame.display.set_mode(screen_size)
	mario_main_menu_pic_load = pygame.image.load('./mario_pics/super_mario_logo.png')
	mario_main_menu_pic = pygame.transform.scale(mario_main_menu_pic_load, [500, 200])
	main_menu_x = 50
	main_menu_y = 50
	mario = Mario(screen)
	background = Background(screen, './mario_pics/full_background_no_sky.png', mario, 0)
	main_menu_background = Background(screen, './mario_pics/full_background_no_sky.png', mario, 300)
	question_blocks = Group()
	physics = Physics()
	# first_goomba = Goomba(screen)
	enemies = Group()
	dead_enemies = Group()
	stars = Group()
	game_on = True
	tick = 0
	power_timer = 0
	background_color = (93,148,251)
	main_menu_font = pygame.font.Font('./mario_pics/8_bit_pusab.ttf', 10)
	star_game_text = main_menu_font.render('Press SPACE to Start.', False, (0,0,0))
	start_text_x = 200
	start_text_y = 250
	game_over_font = pygame.font.Font('./mario_pics/8_bit_pusab.ttf', 25)
	main_menu = True
	start_game = False
	
	for i in background.block_locations:
		question_blocks.add(Block(screen, mario.speed, i))
	# for block in question_blocks:
	# 	stars.add(Star(screen, block.x))
	r = randint(150, 255)
	g = randint(150,255)
	b = randint(150,255)
	#//////////////////////////////
	#////////MUSICnSOUNDS/////////
	#////////////////////////////
	theme_song_load = pygame.mixer.music.load('./sounds/mario_theme.wav')
	theme_song = pygame.mixer.music.play(-1)
	# star_power_song_load = pygame.mixer.music.load('./sounds/mario_dubstep.wav')
	star_power_song = pygame.mixer.Sound('./sounds/mario_dubstep.wav')
	star_power_song.set_volume(.2)
	power_up_sound = pygame.mixer.Sound('./sounds/smb_powerup.wav')
	death_sound = pygame.mixer.Sound('./sounds/smb_mariodie.wav')
	
	
	while game_on == True:

		# print main_menu
		if main_menu == True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == 32:
						start_game = True
			if start_game:
				if main_menu_background.y > 0:
					main_menu_background.y -= 1
					main_menu_y -= 1
					start_text_y -= 1
				elif main_menu_background.y == 0:
					main_menu = False

			
			screen.fill(background_color)	
			screen.blit(mario_main_menu_pic, (main_menu_x, main_menu_y))
			screen.blit(star_game_text, [start_text_x, start_text_y])
			main_menu_background.draw_background(mario)
				# pygame.display.flip()
	
		# print tick
		elif main_menu == False:
			for i in background.goomba_spawn_points:
				if background.x == i:
					enemies.add(Goomba(screen))
				if background.x < i:
					background.goomba_spawn_points.remove(i)
			check_events(background, mario, screen)
			screen.fill(background_color)
			background.draw_background(mario)
			for star in stars:
				star.draw_me(background, physics, question_blocks, mario)
			for block in question_blocks:
				block.draw_block(background)
			for block in question_blocks:
				if block.x <= mario.x + 27 and block.x >= mario.x:
					if mario.hit_block and block.power_up_remaining > 0:
						stars.add(Star(screen, block.x))
						mario.hit_block = False
						block.power_up_remaining -= 1
					elif block.power_up_remaining <= 0:
						mario.hit_block = False
			mario.draw_mario(physics, background, question_blocks, stars)
			# question_block.draw_block(background)
			# print enemies
			# print question_block.y		
			for enemy in enemies:
				enemy.draw_goomba(mario, physics, background)
				mario.check_mario_is_alive(background, enemy, death_sound)
			for enemy in dead_enemies:
				enemy.dead = True
				enemy.draw_goomba(mario, physics, background)
			if mario.star_power:
				theme_song = pygame.mixer.music.pause()
				star_power_song.play()
				power_timer += 1
				mario.max_jump_height = 100
				if power_timer == 10:
					mario.scale += 15
					background.floor -= 14
				elif power_timer == 20:
					mario.scale += 15
					background.floor -= 14
				elif power_timer == 30:
					mario.scale += 15
					background.floor -= 14
				# star_power_song = pygame.mixer.music.play(-1)
				background_color = (r, g, b)
				if tick % 5 == 0:
					r += 10
					g += 15
					b += 16
				if r > 230:
					r -= 150
				if g > 230:
					g -= 150
				if b > 230:
					b -= 150
				for enemy in enemies:
					distance_from_enemy = fabs(mario.x - enemy.x) + fabs(mario.y - enemy.y)
					if distance_from_enemy < 100:
						enemy.dead == True
						dead_enemies.add(enemy)
						# screen.blit(goomba_smush_load, [200, 150])
						enemies.remove(enemy)
				# for enemy in dead_enemies:
				# 	screen.blit(goomba_smush_load, [enemy.x,enemy.y])
				if power_timer > 600:
					mario.star_power = False
					power_timer = 0
					background.floor = 290
					mario.max_jump_height = 163
					background_color = (93,148,251)
					star_power_song.stop()
					theme_song = pygame.mixer.music.unpause()
			if mario.alive == False:
				game_over_text = game_over_font.render("GAME OVER!", False, (0,0,0))
				screen.blit(game_over_text, [150,150])
				theme_song = pygame.mixer.music.stop()
			# print background.x
			# first_goomba.draw_goomba(mario)
		pygame.display.flip()
			
			

run_game()		

	