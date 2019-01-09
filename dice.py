
import random

class Dice(object):

	def __init__(self, name, sides=6):
		self._name=name
		self._sides=sides

	@property
	def get_name(self):
		return self._name

    
	def roll(self):

		return random.choice(range(1, self._sides+1))


