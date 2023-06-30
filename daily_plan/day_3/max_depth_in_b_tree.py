def maxDepth(self, root: Optional[TreeNode]) -> int:
    def dfs(root):
        if(not root):
            return 0

        left = dfs(root.left)
        right = dfs(root.right)

        max_depth = max(left, right) + 1

        return max_depth


    return dfs(root)
