class Settings(object):
	""" A class to store all settings for Alien Invasion """
	
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 750
		self.bg = 25,25,50
		self.ship_speed_factor = 3
		self.ship_limit = 3
		
		# bullet settings
		self.bullet_speed_factor = 4
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullets_allowed = 1000
		self.alien_speed_factor = 2
		# direction 1 represents right , -1 represents left
		self.fleet_direction = 1
		self.fleet_drop_speed = 12
		
                # background image
                self.bg_image = "assets/back46.png" 
		

