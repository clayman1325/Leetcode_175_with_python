def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def dfs(root):
        if(not root):
            return [True, 0]

        left = dfs(root.left)
        right = dfs(root.right)
        height_dif = abs(left[1] - right[1])
        max_height = max(left[1], right[1]) + 1
        balanced = left[0] and right[0] and height_dif < 2

        return [balanced, max_height]

    return dfs(root)[0]