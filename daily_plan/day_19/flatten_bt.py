class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def preorder(root):
          if not root:
            return None

          left = None
          right = None
          if root.left: left = preorder(root.left)
          if root.right: right = preorder(root.right)

          if left:
            left_tail = left
            while left_tail.right:
              left_tail = left_tail.right
            left_tail.right = right
            root.right = left
          if root.left: root.left = None