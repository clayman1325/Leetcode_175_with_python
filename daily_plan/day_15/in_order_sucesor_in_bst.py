
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        def find_successor(root):
            if not root:
                return
            if not root.left:
                return root
            return find_successor(root.left)

        def in_order(root):
            if not root:
                return

            if root.left and root.left == p:
                return root
            elif root.right and root.right == p:
                return root.right
            elif root == p:
                if not root.right:
                    return root
            left = None
            right = None
            if p.val < root.val:
                left  = in_order(root.left)
            else:
                right = in_order(root.right)

            if left == p:
                return root
            if right == p:
                return root
            return left or right

        if p.right:
            node = find_successor(p.right)
        else:
            node = in_order(root)
        if node == p: node = None
        return node

