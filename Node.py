from Hospital import Hospital
import copy
Hospitals = ['0', '1', '2', '3']
PATIENT = 'P'
AMBULANCE = 'A'
WALL = '#'
BLANK = ' '
HOSPITAL = 'H'

LEFT = "Left"
RIGHT = "Right"
TOP = "Top"
BOTTOM = "Bottom"

class Node:
	def __init__(self, status_map, x, y, patients_x, patients_y, hospitals, capacities, parent=None, action=None):
		self.state = status_map
		self.parent = parent
		self.patients_x = patients_x
		self.patients_y = patients_y
		self.capacities = capacities
		self.hospitals = hospitals
		self.path_cost = 0
		self.action = action
		self.x = x
		self.y = y

		if self.parent:
			self.path_cost = parent.get_cost() + 1

	def contains_goal_state(self):
		if len(self.patients_x) == 0:
			return True
		return False
	
	def get_cost(self):
		return self.path_cost;

	def get_children(self):
		children = set()
		self.add_top_child(children)
		self.add_right_child(children)
		self.add_bottom_child(children)
		self.add_left_child(children)
		
		return children


	def add_left_child(self, children):
		i = self.x
		j = self.y

		move = False
		if j == 0:
			move = False
			return
		patients_x = self.patients_x[:]
		patients_y = self.patients_y[:]
		hospitals = self.hospitals
		capacities = self.capacities[:]
		new_state = self.state

		if new_state[i][j-1] == WALL:
			move = False

		elif new_state[i][j-1] == BLANK:
			is_h = False
			is_p = False
			for h in hospitals:
				if h.has_position(i, j-1):
					is_h = True
					break
			for r in range(len(patients_x)):
				if patients_x[r] == i and patients_y[r] == j-1:
					is_p = True
					break
			if is_p == False and is_h == False:
				move = True
			elif is_p == False and is_h == True:
				move = True
			elif is_p == True:
				if j == 1:
					move = False
				elif new_state[i][j-2] == WALL:
					move = False
				elif new_state[i][j-2] == BLANK:
					is_h2 = False
					is_p2 = False
					for h in hospitals:
						if h.has_position(i, j-2):
							is_h2 = True
							break
					for r in range(len(patients_x)):
						if patients_x[r] == i and patients_y[r] == j-2:
							is_p2 = True
							break
					if is_p2 == False and is_h2 == True:
						capacity = 0
						for r in range(len(hospitals)):
							if hospitals[r].has_position(i, j-2):
								capacity = capacities[r]
								if capacity != 0:
									capacities[r] -= 1
								break

						if capacity == 0:
							for r in range(len(patients_x)):
								if patients_x[r] == i and patients_y[r] == j-1:
									patients_y[r] -= 1
									break
						else:
							p = 0
							for r in range(len(patients_x)):
								if patients_x[r] == i and patients_y[r] == j-1:
									p = r
									break
							patients_x.pop(p)
							patients_y.pop(p)
						move = True

					elif is_p2 == False and is_h2 == False:
						for r in range(len(patients_x)):
								if patients_x[r] == i and patients_y[r] == j-1:
									patients_y[r]-=1
									break
						move = True
					else:
						move = False

		if move == True:
			left_node = Node(new_state, i, j-1, patients_x, patients_y, hospitals, capacities, self, LEFT)
			children.add(left_node)


	def add_right_child(self, children):
		i = self.x
		j = self.y

		move = False
		if j == len(self.state[0])-1:
			return
			return
		patients_x = self.patients_x[:]
		patients_y = self.patients_y[:]
		hospitals = self.hospitals
		capacities = self.capacities[:]
		new_state = self.state

		if new_state[i][j+1] == WALL:
			move = False

		elif new_state[i][j+1] == BLANK:
			is_h = False
			is_p = False
			for h in hospitals:
				if h.has_position(i, j+1):
					is_h = True
					break
			for r in range(len(patients_x)):
				if patients_x[r] == i and patients_y[r] == j+1:
					is_p = True
					break
			if is_p == False and is_h == False:
				move = True
			elif is_p == False and is_h == True:
				move = True
			elif is_p == True:
				if j == (len(self.state[0])-2):
					move = False
				elif new_state[i][j+2] == WALL:
					move = False
				elif new_state[i][j+2] == BLANK:
					is_h2 = False
					is_p2 = False
					for h in hospitals:
						if h.has_position(i, j+2):
							is_h2 = True
							break
					for r in range(len(patients_x)):
						if patients_x[r] == i and patients_y[r] == j+2:
							is_p2 = True
							break
					if is_p2 == False and is_h2 == True:
						capacity = 0
						for r in range(len(hospitals)):
							if hospitals[r].has_position(i, j+2):
								capacity = capacities[r]
								if capacity != 0:
									capacities[r] -= 1
								break

						if capacity == 0:
							for r in range(len(patients_x)):
								if patients_x[r] == i and patients_y[r] == j+1:
									patients_y[r] += 1
									break
						else:
							p = 0
							for r in range(len(patients_x)):
								if patients_x[r] == i and patients_y[r] == j+1:
									p = r
									break
							patients_x.pop(p)
							patients_y.pop(p)
						move = True

					elif is_p2 == False and is_h2 == False:
						for r in range(len(patients_x)):
							if patients_x[r] == i and patients_y[r] == j+1:
								patients_y[r] += 1
								break
						move = True
					else:
						move = False
		if move == True:
			right_node = Node(new_state, i, j+1, patients_x, patients_y, hospitals, capacities, self, RIGHT)
			children.add(right_node)

	def add_top_child(self, children):
		i = self.x
		j = self.y

		move = False
		if i == 0:
			return
		patients_x = self.patients_x[:]
		patients_y = self.patients_y[:]
		hospitals = self.hospitals
		capacities = self.capacities[:]
		new_state = self.state

		if new_state[i-1][j] == WALL:
			move = False

		elif new_state[i-1][j] == BLANK:
			is_h = False
			is_p = False
			for h in hospitals:
				if h.has_position(i-1, j):
					is_h = True
					break
			for r in range(len(patients_x)):
				if patients_x[r] == i-1 and patients_y[r] == j:
					is_p = True
					break
			if is_p == False and is_h == False:
				move = True
			elif is_p == False and is_h == True:
				move = True
			elif is_p == True:
				if i == 1:
					move = False
				elif new_state[i-2][j] == WALL:
					move = False
				elif new_state[i-2][j] == BLANK:
					is_h2 = False
					is_p2 = False
					for h in hospitals:
						if h.has_position(i-2, j):
							is_h2 = True
							break
					for r in range(len(patients_x)):
						if patients_x[r] == i-2 and patients_y[r] == j:
							is_p2 = True
							break
					if is_p2 == False and is_h2 == True:
						capacity = 0
						for r in range(len(hospitals)):
							if hospitals[r].has_position(i-2, j):
								capacity = capacities[r]
								if capacity != 0:
									capacities[r] -= 1
								break

						if capacity == 0:
							for r in range(len(patients_x)):
								if patients_x[r] == i-1 and patients_y[r] == j:
									patients_x[r] -= 1
									break
						else:
							p = 0
							for r in range(len(patients_x)):
								if patients_x[r] == i-1 and patients_y[r] == j:
									p = r
									break
							patients_x.pop(p)
							patients_y.pop(p)
						move = True

					elif is_p2 == False and is_h2 == False:
						for r in range(len(patients_x)):
							if patients_x[r] == i-1 and patients_y[r] == j:
								patients_x[r] -= 1
								break
						move = True
					else:
						move = False
		
		if move == True:
			top_node = Node(new_state, i-1, j, patients_x, patients_y, hospitals, capacities, self, TOP)
			children.add(top_node)

	def add_bottom_child(self, children):
		i = self.x
		j = self.y

		move = False
		if i == (len(self.state)-1):
			return
		patients_x = self.patients_x[:]
		patients_y = self.patients_y[:]
		hospitals = self.hospitals
		capacities = self.capacities[:]
		new_state = self.state

		if new_state[i+1][j] == WALL:
			move = False

		elif new_state[i+1][j] == BLANK:
			is_h = False
			is_p = False
			for h in hospitals:
				if h.has_position(i+1, j):
					is_h = True
					break
			for r in range(len(patients_x)):
				if patients_x[r] == i+1 and patients_y[r] == j:
					is_p = True
					break
			if is_p == False and is_h == False:
				move = True
			elif is_p == False and is_h == True:
				move = True
			elif is_p == True:
				if i == (len(self.state)-2):
					move = False
				elif new_state[i+2][j] == WALL:
					move = False
				elif new_state[i+2][j] == BLANK:
					is_h2 = False
					is_p2 = False
					for h in hospitals:
						if h.has_position(i+2, j):
							is_h2 = True
							break
					for r in range(len(patients_x)):
						if patients_x[r] == i+2 and patients_y[r] == j:
							is_p2 = True
							break
					if is_p2 == False and is_h2 == True:
						capacity = 0
						for r in range(len(hospitals)):
							if hospitals[r].has_position(i+2, j):
								capacity = capacities[r]
								if capacity != 0:
									capacities[r] -= 1
								break

						if capacity == 0:
							for r in range(len(patients_x)):
								if patients_x[r] == i+1 and patients_y[r] == j:
									patients_x[r] += 1
									break
						else:
							p = 0
							for r in range(len(patients_x)):
								if patients_x[r] == i+1 and patients_y[r] == j:
									p = r
									break
							patients_x.pop(p)
							patients_y.pop(p)
						move = True

					elif is_p2 == False and is_h2 == False:
						for r in range(len(patients_x)):
							if patients_x[r] == i+1 and patients_y[r] == j:
								patients_x[r] += 1
								break
						move = True
					else:
						move = False

		if move == True:
			bottom_node = Node(new_state, i+1, j, patients_x, patients_y, hospitals, capacities, self, BOTTOM)
			children.add(bottom_node)


	def get_string(self):
		l = ""
		for i in range(len(self.patients_x)):
			l += str(self.patients_x[i])
			l += str(self.patients_y[i])
		l += str(self.x)
		l += str(self.y)
		return l

	def get_state(self):
		info = list()
		hospitals_x = list()
		hospitals_y = list()
		for i in range(len(self.hospitals)):
			if self.capacities[i] != 0:
				hospitals_x.append(self.hospitals[i].x)
				hospitals_y.append(self.hospitals[i].y)
		info.append(hospitals_x)
		info.append(hospitals_y)
		info.append(self.patients_x)
		info.append(self.patients_y)
		return info