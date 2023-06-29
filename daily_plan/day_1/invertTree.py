def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    def dfs(root):
        if(root and root.left is None and root.right is None):
            return root

        left = None
        right = None
        if(root and root.right): left = dfs(root.right)
        if(root and root.left):  right = dfs(root.left)

        if(root):
            root.left  = left
            root.right = right

        return root

    return dfs(root)
