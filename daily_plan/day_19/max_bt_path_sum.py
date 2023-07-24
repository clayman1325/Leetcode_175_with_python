class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
      def dfs(root):
          if not root:
              return [0, -10000]

          left = dfs(root.left)
          right = dfs(root.right)

          left[0] = max(left[0], 0)
          right[0] = max(right[0], 0)

          prev_max = max(left[1], right[1])
          next_val = max(root.val, root.val + left[0], root.val + right[0])
          max_val = max(prev_max, root.val, next_val)
          max_val = max(max_val, root.val + left[0] + right[0], )
          return [next_val, max_val]

      if not root: return root
      if not root.left and not root.right: return root.val
      return dfs(root)[1]