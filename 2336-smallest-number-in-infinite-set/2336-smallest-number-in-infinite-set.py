import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.current = 1
        self.heap = []
        self.added = set()

    def popSmallest(self):
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.added.remove(smallest)
            return smallest

        smallest = self.current
        self.current += 1
        return smallest

    def addBack(self, num):
        if num < self.current and num not in self.added:
            heapq.heappush(self.heap, num)
            self.added.add(num)