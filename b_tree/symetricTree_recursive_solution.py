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
    def isSymmetric(self, root):
        def isTreeSymmetric(leftRoot, rightRoot):
            if leftRoot is None and rightRoot is None: return True
            if (leftRoot is None) or (rightRoot is None): return False
            if leftRoot.val != rightRoot.val: return False

            return isTreeSymmetric(leftRoot.left, rightRoot.right) and isTreeSymmetric(leftRoot.right, rightRoot.left)

        return isTreeSymmetric(root.left, root.right)

# Pseudo code:
# Build left tree and right tree
# Left tree in inorder transversal     right in post order transversal
# Check both are equal
