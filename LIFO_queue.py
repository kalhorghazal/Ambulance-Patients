import copy

class LIFO_queue:
	def __init__(self):
		self.dataset = []

	def enqueue(self, data):
		self.dataset.append(data)

	def dequeue(self):
		if self.is_empty() == True:
			return
		data = self.dataset[len(self.dataset)-1]

		self.dataset.pop(len(self.dataset)-1)

		return data

	def initialize(self, data):
		self.enqueue(data)

	def is_empty(self):
		if len(self.dataset) == 0:
			return True
		return False