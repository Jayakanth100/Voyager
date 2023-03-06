import pygame
import random

class events():

	def __init__( self, SCR_W, SCR_H, screen):

		# game_over_state, run, game_paused_state, etc etc
		# game_state = "RUN" or "PAUSE" or "WHATNOT"
	
		self.SCR_W = SCR_W  # screen width
		self.SCR_H = SCR_H  # screen height
		self.sprite_spd = 10  # player velocity
		self.ctrl_sp = 50	 # control area
		self.sprite = 0

		# background
		self.screen = screen
		self.bg = pygame.image.load("assets/8B blu space.jpg")
		self.bg1 = pygame.transform.scale( self.bg, ( self.SCR_W, self.SCR_H))
		self.bg2 = pygame.transform.flip( self.bg, True, False)
		self.bg2 = pygame.transform.scale( self.bg2, ( self.SCR_W, self.SCR_H))

		# font
		self.fnt = pygame.font.Font('./assets/fonts/zcool.ttf', 18)

		# explosion anime
		expld_sprite_names = [ 'assets/red_explosion/_1.png', 'assets/red_explosion/_2.png',
						'assets/red_explosion/_3.png', 'assets/red_explosion/_4.png',
						'assets/red_explosion/_5.png', 'assets/red_explosion/_6.png',
						'assets/red_explosion/_7.png',  'assets/red_explosion/_7.png',
						'assets/red_explosion/_7.png' ] #dummy values to keep things 'in' index (-_-)

		self.explds = list(map( pygame.image.load, expld_sprite_names))
		self.explds = list(map( lambda x : pygame.transform.scale( x, ( 100, 103)), self.explds))

		# asteroid
		self.droid_y = (60,70,85,100,127,154,169,175,181,193,200,210,235,249,269,278,290,300,321,346,365,378,391,400)
		self.droid_size = ((25,25),(35,30),(45,40),(55,40),(55,40),(65,50),(75,60),(90,65),(100,70))


	def reset(self):

		# game attributes and states
		self.bg1_pos = 0
		self.bg2_pos = self.SCR_W
		self.run = False
		self.game_over_state = False
		self.score = 0
		# self.move_up = False
		# self.move_down = False
		self.expld_ndx = 0

		self.droids = []

	def load_sprite( self, sprite):

		self.sprite,self.sprite_up,self.sprite_down = sprite,sprite,sprite
		self.sprite_area = self.sprite.get_rect(center = ( self.ctrl_sp, 232))

		self.sprite_up = pygame.transform.rotate( self.sprite_up, 15)
		self.sprite_up_area = self.sprite_up.get_rect(center = ( self.ctrl_sp, 232))


		self.sprite_down = pygame.transform.rotate( self.sprite_down, -15)
		self.sprite_down_area = self.sprite_down.get_rect(center = ( self.ctrl_sp, 232))


	def spawn_droids(self):

		Y = random.choice(self.droid_y)
		size = random.choice(self.droid_size)
		droid = pygame.image.load('assets/droid1.png')

		# toppling effect
		if random.choice((True,False)):
			droid = pygame.transform.rotate( droid, -15)
		elif random.choice((True,False)):
			droid = pygame.transform.rotate( droid, 15)
	
		# horizontal flip
		if random.choice((True,False)):
			droid = pygame.transform.flip( droid, True, False)
		
		droid = pygame.transform.scale( droid, size)
		droid_area = droid.get_rect( center = ( self.SCR_W + 100, Y))
		self.droids.append(( droid, droid_area))

	def collision(self):

		midpoint = lambda xy1, xy2 : ( ( ( xy1[0] + xy2[0] )/2 ), ( ( xy1[1] + xy2[1] )/2 ) )

		for droid in self.droids:

			droid = droid[1]

			if self.sprite_area.collidepoint(droid.midbottom):
				return True

			if self.sprite_area.collidepoint(droid.midleft):
				return True

			if self.sprite_area.collidepoint(droid.midright):
				return True

			if self.sprite_area.collidepoint(droid.midtop):
				return True

			if self.sprite_area.collidepoint( midpoint( droid.midtop, droid.midleft)):
				return True

			if self.sprite_area.collidepoint( midpoint( droid.midbottom, droid.midleft)):
				return True

		return False

	def display_explosion( self, xy):

		if self.expld_ndx >= 6:
			pygame.time.wait(2000)
			self.run = False

		expld_area = self.explds[self.expld_ndx].get_rect( center = xy)
		self.expld_ndx += 1
		self.screen.blit( self.explds[self.expld_ndx], expld_area)
		return True

	def display_game_over(self):

		game_over_img = pygame.image.load('assets/game over yellow.png')
		game_over_img = pygame.transform.scale( game_over_img, ( 300, 150))
		game_over_rect = game_over_img.get_rect( center = ( 350, 232))
		self.screen.blit( game_over_img, game_over_rect)


	def display_backdrop(self):

		self.screen.blit( self.bg1, (self.bg1_pos, 0))
		self.screen.blit( self.bg2, (self.bg2_pos , 0))

	def display_score( self, score_text, score_value):
		score = self.fnt.render( score_text + str(score_value), True, (255, 255, 255))
		score_area = score.get_rect(center = ( self.SCR_W - 100, 20))
		self.screen.blit( score, score_area)
		
	def move_backdrop( self, spd):

		self.bg1_pos -= spd
		self.bg2_pos -= spd

		if self.bg1_pos < - self.SCR_W:
			self.bg1_pos =  self.SCR_W
		if self.bg2_pos < - self.SCR_W:
			self.bg2_pos =  self.SCR_W

	def display_player( self, move_up, move_down):

		if self.game_over_state:
			self.display_explosion(self.sprite_area.center)

		elif move_down:
			self.screen.blit( self.sprite_down,  self.sprite_down_area)

		elif move_up:
			self.screen.blit( self.sprite_up,  self.sprite_up_area)

		else:
			self.screen.blit( self.sprite,  self.sprite_area)

	def move_player( self, move_up, move_down):

		if move_up and self.sprite_area.centery >= 30:
			self.sprite_area.centery = self.sprite_area.centery - self.sprite_spd
			self.sprite_up_area.centery = self.sprite_up_area.centery - self.sprite_spd
			self.sprite_down_area.centery = self.sprite_down_area.centery - self.sprite_spd

		if move_down and self.sprite_area.centery <= self.SCR_H - 30 :
			self.sprite_area.centery = self.sprite_area.centery + self.sprite_spd
			self.sprite_up_area.centery = self.sprite_up_area.centery + self.sprite_spd
			self.sprite_down_area.centery = self.sprite_down_area.centery + self.sprite_spd

	def display_droids(self):

		for droid in self.droids:  	# droid has (droid_surface,droid_area)
			self.screen.blit(droid[0], droid[1])

	def move_droids( self, spd):

		for droid in self.droids:
			droid[1].centerx -= spd

	def display_pause_text(self):

		fnt = pygame.font.Font('./assets/fonts/zcool.ttf', 24)
		pause_txt = fnt.render( "PRESS SPACE TO RESUME", True, (255, 255, 255))
		pause_txt_area = pause_txt.get_rect( center = ( 350, 232))
		self.screen.blit( pause_txt, pause_txt_area)
