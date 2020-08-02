import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	""" A class to manage bullets fired from ship """
	
	def __init__(self,ai_settings,screen,ship):
		""" Create bullet object at the ships current location """
		
		super(Bullet,self).__init__()
		self.screen = screen 
		
		# Create a bullet rect at (0,0) and then set correct position 
		#self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
		self.image= pygame.image.load('assets/bullet2.png')
		self.rect = self.image.get_rect()
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		# store the bullets position as a decimal value
		self.y = float(self.rect.y)
		
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
		
	def update(self):
		"""Move the bullet up the screen"""
		# update the deimal position of the bullet.
		self.y -= self.speed_factor
		self.rect.y = self.y
	def draw_bullet(self):
		""" Draw the bullet to the screen"""
		#pygame.draw.rect(self.screen,self.color,self.rect)
		self.screen.blit(self.image,self.rect)
		
