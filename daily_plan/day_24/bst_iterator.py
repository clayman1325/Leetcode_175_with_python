class BSTIterator:
    def __init__(self, root: TreeNode):

        # Stack for the recursion simulation
        self.stack = []

        # Remember that the algorithm starts with a call to the helper function
        # with the root node as the input
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):

        # For a given node, add all the elements in the leftmost branch of the tree
        # under it to the stack.
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """

        # Node at the top of the stack is the next smallest element
        topmost_node = self.stack.pop()

        # Need to maintain the invariant. If the node has a right child, call the
        # helper function for the right child
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0
    def find_child(self, root, pointer):
        if not root: return False
        if root.val == pointer.val:
            return pointer

        left = self.find_child(root.left, pointer)
        right = self.find_child(root.right, pointer)

        if left and left.val == pointer.val and left.val < root.val: return root
        if right and right.val == pointer.val and right.val < root.val: return root

        return left or right
    def find_min(self, root):
        if not root.left:
            return root
        return self.find_min(root.left)
    def find_max(self, root):
        if not root.right:
            return root
        return self.find_max(root.right)

    def __init__(self, root: Optional[TreeNode]):
        self.pointer = self.find_min(root)

        max_val = self.find_max(root).val
        self.max = max_val

        self.root = root


    def next(self) -> int:
        pointer_value = self.pointer.val
        if pointer_value == self.max: self.max = False

        if self.pointer.right:
            self.pointer = self.find_min(self.pointer.right)
        else:
            self.pointer = self.find_child(self.root, self.pointer)
        return pointer_value


    def hasNext(self) -> bool:
        return True if self.max else False