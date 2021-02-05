
class Hospital:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def has_position(self, x, y):
		if self.x == x and self.y == y:
			return True
		return False