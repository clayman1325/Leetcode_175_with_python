class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def inOrderTransverse(root):
            if root is None:
                return []

            left = inOrderTransverse(root.left) + ["l"]
            left.append(root.val)
            right = inOrderTransverse(root.right) + ["r"]
            left += "None" if right is None else right

            return left
        result = []
        def postOrderTransverse(root):
            if root is None:
                return []

            right = postOrderTransverse(root.right) + ["l"]
            right.append(root.val)
            left = postOrderTransverse(root.left) + ["r"]
            right += "None" if left is None else left

            return right

        left_result = inOrderTransverse(root.left)
        right_result = postOrderTransverse(root.right)
        print(left_result, right_result)
        return left_result == right_result