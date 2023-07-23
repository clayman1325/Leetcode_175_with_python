class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
      def current_subTree(node1, node2):
        if node1 is None or node2 is None:
            return node1 is None and node2 is None

        return (node1.val == node2.val and
                current_subTree(node1.left, node2.left) and
                current_subTree(node1.right, node2.right))

      def rec(root, subRoot):
        if current_subTree(root, subRoot):
          return True
        else:
          if not root:
            return False
          return rec(root.left, subRoot) or rec(root.right, subRoot)

      return rec(root, subRoot)