''' this module contains class to define a character player '''
import random
from combat import Combat


class Character(Combat):
	''' Main character player class who will fight with monsters '''
	attack_limit = 10
	experience = 0
	base_hit_points = 10

	def attack(self):
		''' player's overridden attack method '''
		roll = random.randint(1, self.attack_limit)
		if self.weapon == 'sword':
			roll += 1
		elif self.weapon == 'axe':
			roll += 2
		return roll > 4

	def get_weapon(self):
		''' Allow a player to select a weapon of choice '''
		weapon_choice = input("Weapons: [S]word, [A]xe, [B]ow: ").lower()
		if weapon_choice in 'sab':
			if weapon_choice == 's':
				return 'sword'
			elif weapon_choice == 'a':
				return 'axe'
			else:
				return 'bow'
		else:
			return self.get_weapon()

	def __init__(self, **kwargs):
		''' dunder init function to setup a player object '''
		self.name = input("Name: ")
		self.weapon = self.get_weapon()
		self.hit_points = self.base_hit_points
		for key, value in kwargs.items():
			setattr(self, key, value)

	def __str__(self):
		''' return a player instance to a nicely formatter string '''
		return '{}, HP: {}, XP: {}'.format(self.name, self.hit_points, self.experience)

	def rest(self):
		''' method to allow a player to rest '''
		if self.hit_points < self.base_hit_points:
			self.hit_points += 1

	def leveled_up(self):
		''' after gaining experience, levelup function inceases   '''
		return self.experience >= 5