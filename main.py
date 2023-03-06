import pygame
import sys

import mech
import audio
import timer
import menu
import writer

pygame.init()
audio.mixer.init()

SCREEN = pygame.display.set_mode(( 700, 465))
pygame.display.set_caption("Voyager")
pygame.display.set_icon(pygame.image.load("assets/Icon.png"))

shutter = pygame.time.Clock()
game = mech.events( SCR_W = 700, SCR_H = 465, screen = SCREEN)
menu = menu.menu(screen = SCREEN)
sound = audio.sound_tracks( game_background = 'assets/sounds/Contra.mp3',
			game_over = 'assets/sounds/explode.wav', game_intro = 'assets/sounds/Intro.mp3')
clock = timer.timer()

user_data = writer.user_data()
writer.extract_user_data(user_data)

droid_spd, time_interval, sound.audio_on = menu.load_user_settings(user_data.user_settings)

def kill_game():
	user_data.update()
	pygame.quit()
	sys.exit()

while not menu.quit:

	get_run_time = lambda : pygame.time.get_ticks()//1000

	pygame.display.update()
	shutter.tick(30)

	DROID_EVENT = pygame.USEREVENT
	pygame.time.set_timer( DROID_EVENT, time_interval)
	
	play_once = True
	game.reset()
	clock.reset(get_run_time())
	game.load_sprite(menu.get_sprite())
	game_paused_state = False

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			kill_game()

	game.display_backdrop()
	
	if menu.in_settings_screen:
		menu.display_passive_layer()
	else:
		game.display_score( "HIGH SCORE :", user_data.hi_score)
		
	menu.display_title()

	if not menu.in_settings_screen:
		menu.display_main()
	else:
		menu.display_settings()

	keys = pygame.key.get_pressed()

	if menu.in_settings_screen:
		k_f,k_b = keys[pygame.K_DOWN],keys[pygame.K_UP]
	else:
		k_f,k_b = keys[pygame.K_RIGHT],keys[pygame.K_LEFT]

	menu.move_selection( k_b, k_f)
	opt = menu.get_selection()

	if keys[pygame.K_RETURN]:

		if not menu.in_settings_screen:
			if opt == 0:
				game.run = True
			if opt == 1:
				menu.in_settings_screen = True
				menu.reset_option()
			if opt == 2:
				kill_game()

		else:
			if opt == 0:
				droid_spd = 15 if droid_spd == 10 else 10
				time_interval = 300 if time_interval == 700 else 700
				menu.move_sub_selection()
			if opt == 1:
				sound.audio_on = False if sound.audio_on else True
				menu.move_sub_selection()
			if opt == 2:
				menu.move_sub_selection()
			if opt == 3:
				menu.in_settings_screen = False
				menu.reset_option()

		sound.play_click()

	while game.run:

		pygame.display.update()
		shutter.tick(30)
		run_time = get_run_time()

		clock.update_time(run_time)
		game.score = clock.get_time()

		keys = pygame.key.get_pressed()
		k_up,k_down = keys[pygame.K_UP],keys[pygame.K_DOWN]

		for event in pygame.event.get():

			if event.type == DROID_EVENT:
				if not game_paused_state:
					game.spawn_droids()

			if event.type == pygame.QUIT:
				kill_game()

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_SPACE:

					if game_paused_state:
						clock.resume_timer(run_time)
						game_paused_state = False
						audio.mixer.music.unpause()

					else:
						clock.pause_timer()
						menu.display_passive_layer()
						game_paused_state = True
						audio.mixer.music.pause()

		if game_paused_state: 

			game.display_pause_text()
			continue

		# we start displying here
		game.display_backdrop()
		game.display_player( k_up, k_down)
		game.display_droids()
		game.display_score( "YOUR SCORE :", game.score)

		if not game.game_over_state:
			game.move_backdrop(10)
			game.move_droids(droid_spd)
			game.move_player( k_up, k_down)

			if game.score % 67 == 0:
				sound.play_background()

			if game.collision():
				game.game_over_state = True

		else:
			game.display_game_over()
			# sound.play_game_over()
			if play_once:
				play_once = False
				sound.play_game_over()


	if user_data.hi_score < game.score:
		user_data.hi_score = game.score

user_data.update()
pygame.quit() # use me