class Solution:
    def leafSimilar(self, root1, root2):
        def getLeaves(root):
            leaves = []

            def dfs(node):
                if node is None:
                    return

                # Leaf node
                if node.left is None and node.right is None:
                    leaves.append(node.val)
                    return

                dfs(node.left)
                dfs(node.right)

            dfs(root)
            return leaves

        return getLeaves(root1) == getLeaves(root2)