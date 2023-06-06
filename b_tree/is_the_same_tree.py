class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def in_order_trasversal(root):
            if(root is None):
                return []

            left = in_order_trasversal(root.left) + ["l"]
            left.append(root.val)
            right = in_order_trasversal(root.right) + ["r"]
            left = left + right

            return left

        return in_order_trasversal(p) == in_order_trasversal(q)