from collections import deque

class OPTFF:
    members: set
    max_size: int
    curr_size: int
    misses: int
    requests: list
    index: int
    positions: dict

    def __init__(self, size, requests):
        self.members = set()
        self.max_size = size
        self.curr_size = 0
        self.misses = 0
        self.requests = requests
        self.index = 0
        self.positions = {}
        for i, v in enumerate(requests):
            if v not in self.positions:
                self.positions[v] = deque()
            self.positions[v].append(i)

    def take_requests(self):
        for r in self.requests:
            self.positions[r].popleft()
            if r in self.members:
                continue

            self.misses += 1
            if self.curr_size < self.max_size:
                self.members.add(r)
                self.curr_size += 1
                continue

            member_to_evict = None
            farthest = -1
            for m in self.members:
                q = self.positions[m]
                next_use = q[0] if len(q) > 0 else 10**18
                if next_use > farthest:
                    farthest = next_use
                    member_to_evict = m

            self.members.remove(member_to_evict)
            self.members.add(r)
