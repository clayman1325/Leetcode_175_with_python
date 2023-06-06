class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if(root is None):
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            val   = max(left, right) + 1

            return val

        return dfs(root)