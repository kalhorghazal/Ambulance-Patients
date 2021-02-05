import copy
import math
from HEAP_queue import HEAP_queue
from Node import Node

SUCCESS = True
FAILURE = False

class A_STAR:
	def __init__(self, status_map, ambulance_x, ambulance_y, patients_x, patients_y, hospitals, capacities):
		self.number_of_unique_states = 0
		self.number_of_states = 0
		self.path_cost = 0
		self.inital_node = Node(status_map, ambulance_x, ambulance_y, patients_x, patients_y, hospitals, capacities)
		self.frontier = HEAP_queue()
		self.explored = set()
		self.unique_states = set()
		self.goal_node = None

	def f(self, node):
		return self.g(node) + self.h2(node)

	def g(self, node):
		return node.path_cost

	def h(self, node):
		hospitals_x = node.get_state()[0]
		hospitals_y = node.get_state()[1]
		patients_x = node.get_state()[2]
		patients_y = node.get_state()[3]

		sum_distance = 0
		for i in range(len(patients_y)):
			min_distance = math.inf

			for j in range(len(hospitals_x)):
				distance = abs(patients_x[i]-hospitals_x[j]) + abs(patients_y[i]-hospitals_y[j])
				if distance < min_distance:
					min_distance = distance

			sum_distance += min_distance

		return sum_distance


	def h2(self, node):
		patients_x = node.get_state()[2]
		patients_y = node.get_state()[3]

		distances = []
		sum_distance = 0
		for i in range(len(patients_y)):
			distance = abs(patients_x[i]-node.x) + abs(patients_y[i]-node.y)

			sum_distance += distance
			distances.append(distance)
		if len(distances) == 0:
			return 0
		return min(distances)


	def play(self):
		node = self.inital_node

		if node.contains_goal_state():
			self.path_cost= node.path_cost
			return SUCCESS

		self.frontier.initialize(node, self.f(node))

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
				self.path_cost= node.path_cost
				return SUCCESS

			for child in node.get_children():
				if not child.get_string() in self.explored:

					self.frontier.enqueue(child, self.f(child))

		return FAILURE

	def show_result(self):
		print("***A_STAR Search***")
		print("Path Cost: " + str(self.path_cost))
		print("Number of Visited States: " + str(self.number_of_states))
		print("Number of Unique Visited States: " + str(self.number_of_unique_states))