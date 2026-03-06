from collections import OrderedDict

class LRU:
    members: OrderedDict
    max_size: int
    curr_size: int
    misses: int

    def __init__(self, size):
        self.members = OrderedDict()
        self.max_size = size
        self.curr_size = 0
        self.misses = 0

    def take_request(self, request):
        if request in self.members:
            self.members.move_to_end(request)
        else:
            self.misses += 1
            if self.curr_size < self.max_size:
                self.members[request] = True
                self.curr_size += 1
            else:
                self.members.popitem(last=False)
                self.members[request] = True