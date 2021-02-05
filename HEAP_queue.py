import heapq

class HEAP_queue:
    def __init__(self):
        self.dataset = []
        self.top = 0

    def enqueue(self, data, criteria):
        heapq.heappush(self.dataset, (criteria, self.top, data))
        self.top += 1

    def dequeue(self):
        return heapq.heappop(self.dataset)[-1]

    def initialize(self, data, criteria):
        self.enqueue(data, criteria)

    def is_empty(self):
        if len(self.dataset) == 0:
            return True
        return False
