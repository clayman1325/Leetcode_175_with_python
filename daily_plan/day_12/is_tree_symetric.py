class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
      def dfs(node_a, node_b):
        if not node_a and node_b: return False
        if node_a and not node_b: return False
        if not node_a and not node_b: return True

        return node_a.val == node_b.val and dfs(node_a.left, node_b.right) and dfs(node_b.left, node_a.right)
      return dfs(root, root)