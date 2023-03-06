class timer():
	
	def __init__(self):
		self.time = 0
		self.laps = 0

	def get_time(self):
		return self.time

	def update_time( self, curr_time):
		self.time = curr_time - self.laps

	def reset( self, curr_time):
		self.laps = curr_time
		self.time = 0

	def pause_timer(self):
		self.paused_at = self.time

	def resume_timer( self, curr_time):
		self.laps = curr_time - self.paused_at