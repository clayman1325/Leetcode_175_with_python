class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root): return []
        bfs = []
        q = []
        q.append(root)
        level = 0

        while(len(q) > 0):
            limit = len(q)
            level_bfs = []
            for x in range(limit):
                element = q.pop(0)
                if(element): level_bfs.append(element.val)
                if(element and element.left): q.append(element.left)
                if(element and element.right): q.append(element.right)
            bfs.append(level_bfs)
            level += 1
        return bfs