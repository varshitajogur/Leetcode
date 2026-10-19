import heapq

class Solution:
    def totalCost(self, costs, k, candidates):
        n = len(costs)

        # If candidate ranges overlap
        if 2 * candidates >= n:
            heap = []

            for i in range(n):
                heapq.heappush(heap, (costs[i], i))

            total = 0

            for _ in range(k):
                cost, index = heapq.heappop(heap)
                total += cost

            return total

        left_heap = []
        right_heap = []

        left = 0
        right = n - 1

        # Add first candidates workers
        for _ in range(candidates):
            heapq.heappush(left_heap, (costs[left], left))
            left += 1

        # Add last candidates workers
        for _ in range(candidates):
            heapq.heappush(right_heap, (costs[right], right))
            right -= 1

        total = 0

        for _ in range(k):

            # Choose the cheaper worker
            # (cost, index) automatically handles ties
            if left_heap and right_heap:
                if left_heap[0] <= right_heap[0]:
                    cost, index = heapq.heappop(left_heap)

                    if left <= right:
                        heapq.heappush(left_heap, (costs[left], left))
                        left += 1

                else:
                    cost, index = heapq.heappop(right_heap)

                    if left <= right:
                        heapq.heappush(right_heap, (costs[right], right))
                        right -= 1

            elif left_heap:
                cost, index = heapq.heappop(left_heap)

            else:
                cost, index = heapq.heappop(right_heap)

            total += cost

        return total