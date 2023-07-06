class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfsBST(root, k, q):
            if not root:
                return []

            left = dfsBST(root.left, k, q)
            right = dfsBST(root.right, k, q)

            return left + [root.val] + right

        q = []

        result = dfsBST(root, k, q)
        return result[k-1]