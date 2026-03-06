from collections import deque

class FIFO:
    insertion_order: deque
    members: set
    max_size: int
    curr_size: int
    misses: int

    def __init__(self, size):
        self.max_size = size
        self.insertion_order = deque()
        self.members = set()
        self.curr_size = 0
        self.misses = 0

    def take_request(self, request):
        if not request in self.members:
            self.misses += 1
            if self.curr_size < self.max_size:
                self.members.add(request)
                self.insertion_order.append(request)
                self.curr_size += 1
            else:
                removed = self.insertion_order.popleft()
                self.members.remove(removed)
                self.insertion_order.append(request)
                self.members.add(request)