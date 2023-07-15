class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return root

        result = []

        q = [root]
        level = 1
        while(q):
            len_q = len(q)
            cur_level = []
            for i in range(len_q):
                if level % 2 != 0:
                    cur_node = q.pop(0)
                    cur_level.append(cur_node.val)
                else:
                    cur_node = q.pop(0)
                    cur_level.insert(0,cur_node.val)
                if cur_node.left: q.append(cur_node.left)
                if cur_node.right: q.append(cur_node.right)


            level +=1
            result.append(cur_level)
        return result