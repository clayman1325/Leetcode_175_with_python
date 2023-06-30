def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    def dfs(root):
        if(not root):
            return [0, 0]

        left = dfs(root.left)
        right = dfs(root.right)

        max_diameter = max(left[1], right[1])
        max_depth = max(left[0], right[0])
        depth_combination = left[0] + right[0]
        diameter = max(max_diameter, depth_combination)

        return [max_depth + 1, diameter]

    return dfs(root)[1]