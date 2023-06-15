# Question 101. Symmetric Tree 195/199
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Input: root = [1,2,2,null,3,null,3]
# Output: false

# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Symetric tree
#  [         1
#    ,2,        2
# Null,3  ,null,3]

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def inOrderTransverse(root):
            if root is None:
                return []

            left = inOrderTransverse(root.left)
            left.append(root.val)
            right = inOrderTransverse(root.right)
            left += "None" if right is None else right

            return left
        result = []
        def postOrderTransverse(root):
            if root is None:
                return []

            right = postOrderTransverse(root.right)
            right.append(root.val)
            left = postOrderTransverse(root.left)
            right += "None" if left is None else left

            return right

        left_result = inOrderTransverse(root.left)
        right_result = postOrderTransverse(root.right)

        return left_result == right_result

# Pseudo code:
# Build left tree and right tree
# Left tree in inorder transversal     right in post order transversal
# Check both are equal
