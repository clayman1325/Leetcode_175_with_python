# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
      def dfs(root, cur_sum, sum, counter, targetSum, result):
        if not root:
          return

        cur_sum += root.val


        if cur_sum == targetSum: result.append(1)
        if sum_dict.get(cur_sum - targetSum): result.append(sum_dict.get(cur_sum - targetSum))

        sum_dict[cur_sum] = sum_dict.get(cur_sum, 0) + 1

        dfs(root.left, cur_sum, sum_dict, counter, targetSum, result)
        dfs(root.right, cur_sum, sum_dict, counter, targetSum, result)

        sum[cur_sum] -= 1

      if not root: return 0
      if not root.left and not root.right: return 1 if root.val == targetSum else 0

      sum_dict = {}
      cur_sum = 0
      result = []

      dfs(root, cur_sum,sum_dict, 0, targetSum, result)

      return sum(result)