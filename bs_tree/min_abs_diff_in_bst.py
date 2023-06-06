class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(root, list):
            if(root is None):
                return [float('inf'), list]

            list.append(root.val)
            left  = dfs(root.left, list)
            right = dfs(root.right, list)

            min_value = min(left[0], right[0])
            last_node = list.pop()

            for x in list:
                min_value = min(min_value, abs(last_node - x))

            for x in list:
                min_value = min(min_value, abs(last_node - x))

            return [min_value, list]

        return dfs(root, [])[0]