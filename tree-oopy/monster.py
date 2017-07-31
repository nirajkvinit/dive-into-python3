''' This module defines different monster types class '''
import random
from combat import Combat

COLORS = ['yellow', 'red', 'blue', 'green']


class Monster(Combat):
	''' Main Monster class '''
	min_hit_points = 1
	max_hit_points = 1
	min_experience = 1
	max_experience = 1
	weapon = 'sword'
	sound = 'road'

	def __init__(self, **kwargs):
		''' init function to setup a monster with properties '''
		self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
		self.experience = random.randint(self.min_experience, self.max_experience)
		self.color = random.choice(COLORS)

		for key, value in kwargs.items():
			setattr(self, key, value)

	def battlecry(self):
		''' Monster's battle cry '''
		return self.sound.upper()

	def __str__(self):
		''' Return a Monster object to a nicely formatted string '''
		return '{} {}, HP: {}, XP: {}'.format(self.color.title(),
                                        self.__class__.__name__,
                                        self.hit_points,
                                        self.experience)


class Goblin(Monster):
	''' Monster Type - Goblin '''
	max_hit_points = 3
	max_experience = 2
	sound = 'squeak'


class Troll(Monster):
	''' Monster Type - Troll '''
	min_hit_points = 3
	max_hit_points = 5
	min_experience = 2
	max_experience = 6
	sound = 'growl'


class Dragon(Monster):
	''' Monster Type - Dragon '''
	min_hit_points = 5
	max_hit_points = 10
	min_experience = 6
	max_experience = 10
	sound = 'raaaaaa'
