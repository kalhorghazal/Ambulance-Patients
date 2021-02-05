import copy

class FIFO_queue:
	def __init__(self):
		self.dataset = []

	def enqueue(self, data):
		self.dataset.append(data)

	def dequeue(self):
		if self.is_empty() == True:
			return
		data = self.dataset[0]

		self.dataset.pop(0)

		return data

	def initialize(self, data):
		self.enqueue(data)

	def is_empty(self):
		if len(self.dataset) == 0:
			return True
		return False