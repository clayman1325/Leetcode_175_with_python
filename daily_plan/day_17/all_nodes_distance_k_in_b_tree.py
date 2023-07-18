class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def build_adj(adj, root):
            if not root:
                return
            left = root.left.val if root.left else None
            right = root.right.val if root.right else None

            if adj.get(root.val):
                adj[root.val].append(left)
                adj[root.val].append(right)
            else:
                adj[root.val] = [left, right]
            if left:
                if adj.get(left):
                    adj[left].append(root.val)
                else:
                    adj[left] = [root.val]
            if right:
                if adj.get(right):
                    adj[right].append(root.val)
                else:
                    adj[right] = [root.val]

            build_adj(adj, root.left)
            build_adj(adj, root.right)

        adj = {}
        build_adj(adj,root)
        visited = set()
        q = [(target.val,0)]
        level=1
        result=[]

        while(q):
            len_q = len(q)

            for i in range(len_q):
                node = q.pop(0)
                visited.add(node[0])
                if node[1] == k: result.append(node[0])

                if node[0] == 0 or adj.get(node[0]):
                    for neighboor in adj.get(node[0]):
                        if neighboor is not None and neighboor not in visited:
                            q.append((neighboor, level))
                            print(neighboor, q)
            level += 1

        return result