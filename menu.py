import pygame

class menu():

	def __init__(self, screen):

		fnt = pygame.font.Font('./assets/fonts/zcool.ttf', 28)
		large_fnt = pygame.font.Font('./assets/fonts/zcool.ttf', 40)

		self.screen = screen

		play_txt = fnt.render("    PLAY    ", True, (255,255,255))
		play_area = play_txt.get_rect(center = (175,360))
		play_button = fnt.render("    PLAY    ", True, (255,255,255), (0,153,115))
		play_button.set_alpha(80)

		settings_txt = fnt.render("  SETTINGS  ", True, (255,255,255))
		settings_area = settings_txt.get_rect(center = (350,360))
		settings_button = fnt.render("  SETTINGS  ", True, (255,255,255), (0,115,153))
		settings_button.set_alpha(80)

		quit_txt = fnt.render("    QUIT    ", True, (255,255,255))
		quit_area = quit_txt.get_rect(center = (525,360))
		quit_button = fnt.render("    QUIT    ", True, (255,255,255), (153,0,51))
		quit_button.set_alpha(80)

		selected_play_button = fnt.render("    PLAY    ", True, (255,255,255), (0,153,115))
		selected_settings_button = fnt.render("  SETTINGS  ", True, (255,255,255), (0,115,153))
		selected_quit_button = fnt.render("    QUIT    ", True, (255,255,255), (153,0,51))	
	
		self.buttons = ( (play_txt, play_button, selected_play_button, play_area),
					(settings_txt, settings_button, selected_settings_button, settings_area),
					(quit_txt, quit_button, selected_quit_button, quit_area) )

		mode_txt = fnt.render("    MODE    ", True, (255,255,255))
		mode_area = mode_txt.get_rect(center = (175,200))
		mode_button = fnt.render("    MODE    ", True, (255,255,255), (0,115,153))
		mode_button.set_alpha(80)

		BGM_txt = fnt.render("    MUSIC   ", True, (255,255,255))
		BGM_area = BGM_txt.get_rect(center = (175,250))
		BGM_button = fnt.render("    MUSIC   ", True, (255,255,255), (0,115,153))
		BGM_button.set_alpha(80)

		sprite_txt = fnt.render("   SPRITE   ", True, (255,255,255))
		sprite_area = sprite_txt.get_rect(center = (175,320))
		sprite_button = fnt.render("   SPRITE   ", True, (255,255,255), (0,115,153))
		sprite_button.set_alpha(80)

		back_txt = fnt.render("    BACK    ", True, (255,255,255))
		back_area = back_txt.get_rect(center = (175,390))
		back_button = fnt.render("    BACK    ", True, (255,255,255), (0,115,153))
		back_button.set_alpha(80)

		selected_mode_button = fnt.render("    MODE    ", True, (255,255,255), (0,115,153))
		selected_BGM_button = fnt.render("    MUSIC   ", True, (255,255,255), (0,115,153))
		selected_sprite_button = fnt.render("   SPRITE   ", True, (255,255,255), (0,115,153))
		selected_back_button = fnt.render("    BACK    ", True, (255,255,255), (0,115,153))

		self.settings = ( ( mode_txt, mode_button, selected_mode_button, mode_area),
						  ( BGM_txt, BGM_button, selected_BGM_button, BGM_area),
						  ( sprite_txt, sprite_button, selected_sprite_button, sprite_area),
						  ( back_txt, back_button, selected_back_button, back_area))

		ez_txt = fnt.render("    EASY    ", True, (255,255,255))
		ez_area = ez_txt.get_rect(center = (300,200))
		ez_button = fnt.render("    EASY    ", True, (255,255,255), (0,153,115))
		ez_button.set_alpha(80)

		hrd_txt = fnt.render("    HARD    ", True, (255,255,255))
		hrd_area = hrd_txt.get_rect(center = (400,200))
		hrd_button = fnt.render("    HARD    ", True, (255,255,255), (153,0,51))
		hrd_button.set_alpha(80)

		selected_ez_button = fnt.render("    EASY    ", True, (255,255,255), (0,153,115))
		selected_hrd_button = fnt.render("    HARD    ", True, (255,255,255), (153,0,51))

		self.mode_sub = ( ( ez_txt, ez_button, selected_ez_button, ez_area),
						( hrd_txt, hrd_button, selected_hrd_button, hrd_area))

		on_txt = fnt.render("       ON       ", True, (255,255,255))
		on_area = on_txt.get_rect(center = (300,250))
		on_button = fnt.render("       ON       ", True, (255,255,255), (0,153,115))
		on_button.set_alpha(80)

		off_txt = fnt.render("    OFF       ", True, (255,255,255))
		off_area = off_txt.get_rect(center = (400,250))
		off_button = fnt.render("    OFF       ", True, (255,255,255), (153,0,51))
		off_button.set_alpha(80)

		selected_on_button = fnt.render("       ON       ", True, (255,255,255), (0,153,115))
		selected_off_button = fnt.render("    OFF       ", True, (255,255,255), (153,0,51))

		self.BGM_sub = ( ( on_txt, on_button, selected_on_button, on_area),
					   ( off_txt, off_button, selected_off_button, off_area))

		flght = pygame.image.load('assets/flight.png')
		flght = pygame.transform.rotate( flght, -90)
		flght = pygame.transform.scale( flght, ( 35, 38))
		flght_area = flght.get_rect(center = ( 275, 320))

		ufo = pygame.image.load('assets/ufo1.png')
		ufo = pygame.transform.scale( ufo, ( 65, 50))
		ufo_area = ufo.get_rect(center = ( 275, 320))

		arshp = pygame.image.load('assets/airship.png')
		arshp = pygame.transform.scale( arshp, ( 60, 40))
		arshp_area = arshp.get_rect(center = ( 275, 320))

		self.sprites = ( ( flght, flght_area), ( ufo, ufo_area), ( arshp, arshp_area))

		self.title_main = pygame.image.load("assets/title.png")
		self.title_main_area = self.title_main.get_rect( center = (350,200))

		self.title_settings_img = pygame.image.load("assets/gear.png")
		self.title_settings_img = pygame.transform.scale( self.title_settings_img, ( 60, 60))
		self.title_settings_img_area = self.title_settings_img.get_rect( center = (98,100))

		self.title_settings_txt = large_fnt.render(" SETTINGS ", True, (255,255,255))
		self.title_settings_txt_area = self.title_settings_txt.get_rect( center = (220,100))

		self.selector = 0
		self.in_settings_screen = False
		self.quit = False

	def load_user_settings(self, user_settings):

		droid_spd, interval = 10, 700
		audio_on = True
		
		self.sub_selector = user_settings

		if self.sub_selector[0] == 1:
			droid_spd, interval =  15, 300 
		if self.sub_selector[1] == 1:
			audio_on = False			

		return droid_spd, interval, audio_on

	def move_selection( self, k_f, k_b):

		limit = 2

		if self.in_settings_screen:
			limit = 3

		if k_b:
			if self.selector != limit:
				self.selector += 1
			pygame.time.wait(150)

		if k_f:
			if self.selector != 0:
				self.selector -= 1
			pygame.time.wait(150)
		

	def move_sub_selection(self):

		limit = 0
		if self.selector == 0 or self.selector == 1:
			limit = 1
		elif self.selector == 2:
			limit = 2

		if self.sub_selector[self.selector]  == limit:
			self.sub_selector[self.selector] = 0
			pygame.time.wait(150)

		else:
			self.sub_selector[self.selector] += 1
			pygame.time.wait(150)



	def get_selection(self):

		return self.selector

	def get_sub_selection(self):

		return self.sub_selector[self.selector]

	def get_sprite(self):

		return self.sprites[ self.sub_selector[2] ][0]

	def display_options( self, options, key):

		for option in options: 

			if option == options[key]: 
				self.screen.blit( option[2], option[3])
			else:
				self.screen.blit( option[1], option[3])
		
			self.screen.blit( option[0], option[3])

	def display_title(self):

		if self.in_settings_screen:
			self.screen.blit( self.title_settings_txt, self.title_settings_txt_area)
			self.screen.blit( self.title_settings_img, self.title_settings_img_area)
		else:
			self.screen.blit( self.title_main, self.title_main_area)
		
	def display_passive_layer(self):

		temp = pygame.Surface( (700,465), pygame.SRCALPHA)
		temp.set_alpha(25)
		pygame.draw.rect(temp,(255,255,255),temp.get_rect())
		self.screen.blit(temp,(0,0))

	def display_settings(self):

		self.display_options( self.settings, self.selector)
		self.display_options( self.mode_sub, self.sub_selector[0])
		self.display_options( self.BGM_sub, self.sub_selector[1])
		self.display_sprite()

	def display_main(self):

		self.display_options( self.buttons, self.selector)

	def reset_option(self):

		self.selector = 0
		pygame.time.wait(150)

	def display_sprite(self):

		sprite,area = self.sprites[self.sub_selector[2]]
		self.screen.blit(sprite,area)


