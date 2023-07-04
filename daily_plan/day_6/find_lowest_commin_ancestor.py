class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root:
                return False

            left = dfs(root.left)
            right = dfs(root.right)

            mid = root == p or root == q

            if mid and left or mid and right or left and right:
                return root

            return mid or left or right

        result = dfs(root)

        if(result == True):
            result = root
        return result