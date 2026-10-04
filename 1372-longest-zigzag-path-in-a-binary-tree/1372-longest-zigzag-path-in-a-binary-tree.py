class Solution:
    def longestZigZag(self, root):
        self.ans = 0

        def dfs(node):
            if not node:
                return (-1, -1)

            left = dfs(node.left)
            right = dfs(node.right)

            # Start by going left
            go_left = 1 + left[1]

            # Start by going right
            go_right = 1 + right[0]

            self.ans = max(self.ans, go_left, go_right)

            return (go_left, go_right)

        dfs(root)
        return self.ans