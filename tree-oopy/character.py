class Character:
	experience = 0
	hit_points = 10

	def __init__(self, **kwargs):
		self.name = input("Name: ")
		self.weapons = input("Weapons: [S]word, [A]xe, [B]ow")
		for key, value in kwargs.items():
			setattr(self, key, value)