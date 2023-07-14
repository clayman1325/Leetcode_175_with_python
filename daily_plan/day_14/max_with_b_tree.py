class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        level = 1
        position = 1
        width = []
        max_width = 0

        q=[(root, position)]

        while q:
            for _ in range(len(q)):
                cur_node, position = q.pop(0)
                width.append(position)
                if cur_node.left:
                    q.append((cur_node.left, position * 2))
                if cur_node.right:
                    q.append((cur_node.right, position * 2 + 1))

            max_width = max(max_width, width[-1] - width[0])
            width = []
            level += 1

        return max_width + 1