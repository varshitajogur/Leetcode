class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)

        a = 0
        b = 0

        for i in range(2, n + 1):
            current = min(b + cost[i - 1], a + cost[i - 2])
            a = b
            b = current

        return b