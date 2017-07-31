''' Monster Game Main class '''
import sys
from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll


class Game:
	''' Main Class where game is being played '''

	def setup(self):
		''' setup the game '''
		self.player = Character()
		self.monsters = [
                    Goblin(),
                    Troll(),
                    Dragon(),]
		self.monster = self.get_next_monster()


	def get_next_monster(self):
		''' Get a new monster from the monsters list '''
		try:
			return self.monsters.pop()
		except IndexError:
			return None

	def monster_turn(self):
		''' Monster's turn in the game '''
		# check to see if the monster attacks
		if self.monster.attack():
			# if so tell the player
			print("{} is attacking!".format(self.monster))

			# check if the player wants to dodge
			if input("Dodge? Y/N ").lower() == 'y':
				# if so, see if the dodge is successful
				if self.player.dodge():
					# if it is, move on
					print("You dodged the attack!")
				else:
					# if it's not, remove one player hit point
					print("You got hit anyway!")
					self.player.hit_points -= 1
			else:
				print("{} hit you for 1 point: ".format(self.monster))
				self.player.hit_points -= 1
		else:
			# if the monster isn't attacking, thell that to player too.
			print("{} isn't attacking this turn.".format(self.monster))


	def player_turn(self):
		''' player's turn in the game '''
		# let the player attack, rest, or quit
		player_choice = input("[A]ttack, [R]est, [Q]uit? ").lower()

		# if they attack:
		if player_choice == 'a':
			print("You're attacking {}!".format(self.monster))
			# see if the attack is successful
			if self.player.attack():
				# if so, see if the monster dodges
				if self.monster.dodge():
					# if dodged, print that
					print("{} dodged your attack! ".format(self.monster))
				else:
					if self.player.leveled_up():
						# if not dodged, substract the right num of hit points from the monster
						self.monster.hit_points -= 2
					else:
						# if not dodged, substract the right num of hit points from the monster
						self.monster.hit_points -= 1
					print("You hit {} with your {}!".format(self.monster, self.player.weapon))
			else:
				# if not a good attack, tell the player
				print("You missed!")
		# if the rest:
		elif player_choice == 'r':
			# call the player.rest() method
			self.player.rest()
		elif player_choice == 'q':
			# if they quit, exit the game
			sys.exit()
		else:
			# if they pick anything else, re-run this method
			self.player_turn()


	def cleanup(self):
		''' after a monster is killed
			add monster's experience to player's experience
			and get new monster
		'''
		if self.monster.hit_points <= 0:
			self.player.experience += self.monster.experience
			print("You killed {}!".format(self.monster))
			self.monster = self.get_next_monster()


	def __init__(self):
		''' setup and play the game '''
		self.setup()
		while self.player.hit_points and (self.monster or self.monsters):
			print("\n"+"="*20)
			print(self.player)
			self.monster_turn()
			print('-'*20)
			self.player_turn()
			self.cleanup()
			print("\n"+"="*20)

		if self.player.hit_points:
			print("You win!")
		elif self.monsters or self.monster:
			print("You lose!")
		sys.exit()


Game()
