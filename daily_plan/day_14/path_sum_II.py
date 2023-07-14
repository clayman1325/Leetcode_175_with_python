class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root, paths, path, cur_sum, target):
            if not root:
                return
            cur_sum += root.val
            if root and not root.left and not root.right:
                if cur_sum == target:
                    paths.append(path + [root.val])
                return


            dfs(root.left, paths, path + [root.val], cur_sum, target)
            dfs(root.right, paths, path + [root.val], cur_sum, target)
        paths = []
        dfs(root, paths, [], 0, targetSum)
        return paths