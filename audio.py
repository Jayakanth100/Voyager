from pygame import mixer

class sound_tracks():

	def __init__( self, game_over, game_background, game_intro):

		self.audio_on = False
		self.game_over = game_over
		self.game_background = game_background
		self.game_intro = game_intro
		self.click = 'assets/sounds/click.wav'


	def play_sound( self, song):

		if self.audio_on:
			mixer.music.load(song)
			mixer.music.play()

	def play_game_over(self):

		mixer.music.set_volume(0.9)
		self.play_sound(self.game_over)


	def play_background(self):

		mixer.music.set_volume(0.2)
		self.play_sound(self.game_background)

	def play_intro(self):

		mixer.music.set_volume(0.2)
		self.play_sound(self.game_intro)

	def play_click(self):

		mixer.music.set_volume(0.2)
		self.play_sound(self.click)