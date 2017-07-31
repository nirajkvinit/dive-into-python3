''' root class. Players and Monsters inherits properties and functionalities from this class '''
import random


class Combat:
	''' Combat class which contains dodge/attack limits and methods '''
	dodge_limit = 6
	attack_limit = 6

	def dodge(self):
		''' dodge method to randomly determine whether a combatant is dodging or not '''
		roll = random.randint(1, self.dodge_limit)
		return roll > 4

	def attack(self):
		''' attack method to randomly determine whether a combatant is attacking or not '''
		roll = random.randint(1, self.attack_limit)
		return roll > 4
