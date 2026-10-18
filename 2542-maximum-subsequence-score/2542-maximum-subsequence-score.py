import heapq

class Solution:
    def maxScore(self, nums1, nums2, k):
        pairs = list(zip(nums1, nums2))

        # Sort by nums2 in descending order
        pairs.sort(key=lambda x: x[1], reverse=True)

        min_heap = []
        total = 0
        answer = 0

        for num1, num2 in pairs:
            heapq.heappush(min_heap, num1)
            total += num1

            # Keep exactly k elements
            if len(min_heap) > k:
                total -= heapq.heappop(min_heap)

            # num2 is the minimum nums2 among selected elements
            if len(min_heap) == k:
                answer = max(answer, total * num2)

        return answer