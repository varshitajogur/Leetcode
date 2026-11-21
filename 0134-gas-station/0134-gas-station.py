
class Solution:
    def canCompleteCircuit(self, gas, cost):

        total_tank = 0
        current_tank = 0
        start = 0

        for i in range(len(gas)):

            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]

            if current_tank < 0:
                start = i + 1
                current_tank = 0

        if total_tank < 0:
            return -1

        return start
