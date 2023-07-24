
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        result = root
        q = [root]

        while q:
            len_q = len(q)
            for i in range(len_q):
                cur_node = q.pop(0)
                if len(q) > 0: cur_node.next = q[0]
                if cur_node and cur_node.left: q.append(cur_node.left)
                if cur_node and cur_node.right: q.append(cur_node.right)
            cur_node.next = None

        return result