import copy
from LIFO_queue import LIFO_queue
from Node import Node

SUCCESS = True
FAILURE = False

class IDS:
	def __init__(self, status_map, ambulance_x, ambulance_y, patients_x, patients_y, hospitals, capacities):
		self.number_of_unique_states = 0
		self.number_of_states = 0
		self.path_cost = 0
		self.inital_node = Node(status_map, ambulance_x, ambulance_y, patients_x, patients_y, hospitals, capacities)
		self.frontier = LIFO_queue()
		self.explored = set()
		self.unique_states = set()
		self.goal_node = None
		self.min_depth_explored = {}


	def dls(self, node, depth):
		self.number_of_states += 1

		if not node.get_string() in self.unique_states:
			self.unique_states.add(node.get_string())
			self.number_of_unique_states += 1

		if node.contains_goal_state():
			return SUCCESS

		if depth <= 0:
			return FAILURE

		self.min_depth_explored[node.get_string()] = depth

		for child in node.get_children():
			if (not child.get_string() in self.min_depth_explored) or self.min_depth_explored[child.get_string()] < depth-1:

				if self.dls(child, depth-1) == SUCCESS:
					return SUCCESS	
		return FAILURE

	def play(self):
		node = self.inital_node
		self.min_depth_explored = {}
		depth = 1
		while True:
			if self.dls(node, depth) == SUCCESS:
				self.path_cost = depth
				return SUCCESS
			depth +=1
		return FAILURE



	def show_result(self):
		print("***Iterative Deepening Search***")
		print("Path Cost: " + str(self.path_cost))
		print("Number of Visited States: " + str(self.number_of_states))
		print("Number of Unique Visited States: " + str(self.number_of_unique_states))