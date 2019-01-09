
import random

class Dice(object):

	def __init__(self, name):
		self._name=name

	@property
	def get_name(self):
		return self._name

    
	def roll(self):
		return random.choice(range(1, 7))


