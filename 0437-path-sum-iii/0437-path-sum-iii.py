class Solution:
    def pathSum(self, root, targetSum):
        prefix = {0: 1}

        def dfs(node, currentSum):
            if node is None:
                return 0

            currentSum += node.val

            count = prefix.get(currentSum - targetSum, 0)

            prefix[currentSum] = prefix.get(currentSum, 0) + 1

            count += dfs(node.left, currentSum)
            count += dfs(node.right, currentSum)

            prefix[currentSum] -= 1

            return count

        return dfs(root, 0)