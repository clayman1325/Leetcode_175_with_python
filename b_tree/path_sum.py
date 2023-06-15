class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,target, sum):
            if(root is None):
                return False

            sum += root.val

            if(not root.left and not root.right and sum == targetSum):
                return True

            left = dfs(root.left, target, sum)
            right = dfs(root.right, target, sum)

            return left or right

        if(root is None): return False

        return dfs(root,targetSum, 0)


# Pseudocode:
# dfs until leave adding up root val
# if sum eq to target retrun target else 0