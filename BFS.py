import copy
from FIFO_queue import FIFO_queue
from Node import Node

SUCCESS = True
FAILURE = False

class BFS:
	def __init__(self, status_map, ambulance_x, ambulance_y, patients_x, patients_y, hospitals, capacities):
		self.number_of_unique_states = 0
		self.number_of_states = 0
		self.path_cost = 0
		self.inital_node = Node(status_map, ambulance_x, ambulance_y, patients_x, patients_y, hospitals, capacities)
		self.frontier = FIFO_queue()
		self.explored = set()
		self.unique_states = set()
		self.goal_node = None
 
	def play(self):
		node = self.inital_node

		if node.contains_goal_state():
			self.path_cost = node.path_cost
			return SUCCESS

		self.frontier.initialize(node)

		while not self.frontier.is_empty():
				
			node = self.frontier.dequeue()

			self.number_of_states += 1
			if node.get_string() in self.explored:
				continue

			self.explored.add(node.get_string())

			if not node.get_string() in self.unique_states:
				self.unique_states.add(node.get_string())
				self.number_of_unique_states += 1

			if node.contains_goal_state():
				self.path_cost = node.path_cost
				return SUCCESS

			for child in node.get_children():
				if not child.get_string() in self.explored:

					if child.contains_goal_state():
						self.path_cost= child.path_cost
						return SUCCESS

					self.frontier.enqueue(child)

		return FAILURE

	def show_result(self):
		print("***Breadth First Search***")
		print("Path Cost: " + str(self.path_cost))
		print("Number of Visited States: " + str(self.number_of_states))
		print("Number of Unique Visited States: " + str(self.number_of_unique_states))