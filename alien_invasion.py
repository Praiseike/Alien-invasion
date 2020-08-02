"""
Email: Praiseike123@gmail.com
"""

import pygame
from pygame.sprite import Group
import sys
from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf
from alien import Alien
from button import Button




def run_game():
	pygame.init()
	ai_settings = Settings()
	s = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.toggle_fullscreen()
	pygame.display.set_caption("Alien Invasion")
	# Make the Play button.
	play_button = Button(ai_settings,s,"Play")
	
	# Create an instance to store game statistics
	stats = GameStats(ai_settings)
	
	background = pygame.image.load(ai_settings.bg_image)
	# create  a ship 
	ship = Ship(s,ai_settings)
	
	# make a group of bullets and aliens.
	bullets = Group()
	aliens = Group()
	# make an alien
	alien = Alien(ai_settings,s)
	
	# create the fleet of aliens
	gf.create_fleet(ai_settings,ship,s,aliens)	
	
	
	while True: # starting the main loop
		gf.check_events(ai_settings, s, stats, play_button, ship,aliens,bullets)
		
		if stats.game_active:
			# redraw the screen
			ship.update()
			gf.update_bullets(ai_settings,s,ship,aliens,bullets)
			gf.update_aliens(ai_settings,stats,s,ship,aliens,bullets)
		
		
		gf.update_screen(ai_settings,s,stats,ship,aliens,bullets,play_button,background)		
	
run_game()
