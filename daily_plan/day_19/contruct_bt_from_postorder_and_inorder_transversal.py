class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def array_to_tree(left,right):
            if left > right:
                return None

            val = postorder.pop()
            root = TreeNode(val)

            index = inorder_index[val]
            root.right = array_to_tree(index+1, right)
            root.left = array_to_tree(left, index - 1)

            return root

        inorder_index = {}
        for index, value in enumerate(inorder):
            inorder_index[value] = index
        return array_to_tree(0, len(inorder) - 1)