class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # If we reach an empty node, return None
        if root is None:
            return None

        # If root is one of p or q, it can be the LCA
        if root == p or root == q:
            return root

        # Search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # p and q are found in different subtrees
        if left and right:
            return root

        # Return whichever subtree contains p or q
        return left if left else right