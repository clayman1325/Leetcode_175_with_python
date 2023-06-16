def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    node = root
    q = deque([node])
    level = 0
    curr_level = []
    while q:
        n = len(q)
        for _ in range(n):
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
                q.append(curr.right)
                if not level % 2:
                    curr_level.append(curr.left.val)
                    curr_level.append(curr.right.val)
            if level % 2:
                curr.val = curr_level.pop()
        level += 1
    return root