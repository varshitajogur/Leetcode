class Solution:
    def goodNodes(self, root):
        def dfs(node, max_value):
            if not node:
                return 0

            # Check if current node is good
            if node.val >= max_value:
                count = 1
            else:
                count = 0

            # Update maximum value on the path
            max_value = max(max_value, node.val)

            # Check left and right subtrees
            count += dfs(node.left, max_value)
            count += dfs(node.right, max_value)

            return count

        return dfs(root, root.val)