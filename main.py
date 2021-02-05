from BFS import BFS
from IDS import IDS
from A_STAR import A_STAR
from Hospital import Hospital
from time import time

Hospitals = ['0', '1', '2', '3']
PATIENT = 'P'
AMBULANCE = 'A'
WALL = '#'
BLANK = ' '
HOSPITAL = 'H'

SUCCESS = True
FAILURE = False

char_map = []
file = open('test1.txt', 'r')
for x in file:
	x = list(x)
	if x[len(x)-1] == '\n':
		x = x [:len(x)-1]

	char_map.append(x)
file.close()

ambulance_x = 0
ambulance_y = 0
patients_x = list()
patients_y = list()
hospitals = list()
capacities = list()

for i in range(len(char_map)):
	for j in range(len(char_map[0])):
		if char_map[i][j] == AMBULANCE:
			ambulance_x = i
			ambulance_y = j
			char_map[i][j] = BLANK
		elif char_map[i][j] in Hospitals:
			capacity = ord(char_map[i][j]) - ord('0')
			h = Hospital(i, j)
			hospitals.append(h)
			capacities.append(capacity)
			char_map[i][j] = BLANK
		elif char_map[i][j] == PATIENT:
			patients_x.append(i)
			patients_y.append(j)
			char_map[i][j] = BLANK


#bfs = BFS(char_map, ambulance_x, ambulance_y, patients_x, patients_y, hospitals, capacities)
#start = time()
#result = bfs.play()
#finish = time()
#bfs.show_result()

#ids = IDS(char_map, ambulance_x, ambulance_y, patients_x, patients_y, hospitals, capacities)
#start = time()
#result = ids.play()
#finish = time()
#ids.show_result()

a_star = A_STAR(char_map, ambulance_x, ambulance_y, patients_x, patients_y, hospitals, capacities)
start = time()
result = a_star.play()
finish = time()
a_star.show_result()

duration = finish - start
print("Execution Time: " + str(duration))
