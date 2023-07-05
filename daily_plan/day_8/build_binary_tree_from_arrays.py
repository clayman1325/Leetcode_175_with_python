class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def recBuild(preorder, inorder, root_idx):
            print(preorder, inorder)
            if not preorder or not inorder: return None
            if len(preorder) == 1 or len(inorder) == 1: return TreeNode(preorder[0])

            if preorder:
                root = preorder[0]
                new_root = TreeNode(root)
            else:
                new_root = None

            left = None
            right = None

            for idx in range(len(inorder)):
                if inorder[idx] == root:
                    left = inorder[:idx]
                    right = inorder[idx + 1:]

            left = recBuild(preorder[root_idx+1:], left, 0)
            right = recBuild(preorder[root_idx+2:], right, 0)
            new_root.left = left
            new_root.right = right

            return new_root
        result = recBuild(preorder, inorder, 0)
        return result