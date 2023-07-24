class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def array_to_tree(left, right):
            if left > right: return None
            root_val = preorder[preorder_index]
            root = TreeNode(root_val)

            preorder_index += 1

            root.left = array_to_tree(left, inorder_index[root_val] -1)
            root.right = array_to_tree(inorder_index[root_val + 1], right)

            return root

            preorder_index = 0

            inorder_index = {}
            for index, value in enumerate(inorder):
            inorder_index[value] = index

        return array_to_tree(0, len(preorder) - 1)