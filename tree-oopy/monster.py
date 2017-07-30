class Monster:

	def __init__(self, **kwargs):
		self.hit_points = kwargs.get('hit_points', 1)
		self.weapon = kwargs.get('weapon', 'sword')
		self.color = kwargs.get('color', 'yellow')
		self.sound = kwargs.get('sound', 'roar')

	def battlecry(self):
		return self.sound.upper()