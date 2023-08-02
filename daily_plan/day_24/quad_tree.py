class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def rec(grid):
            if len(grid) == 1:
                return Node(val=bool(grid[0][0]), isLeaf=True)

            all_same = all(all(val == grid[0][0] for val in row) for row in grid)
            if all_same:
                return Node(val=bool(grid[0][0]), isLeaf=True)

            node = Node(isLeaf=False)

            n = len(grid)
            mid = n // 2
            top_left = [row[:mid] for row in grid[:mid]]
            top_right = [row[mid:] for row in grid[:mid]]
            bottom_left = [row[:mid] for row in grid[mid:]]
            bottom_right = [row[mid:] for row in grid[mid:]]

            node.topLeft = rec(top_left)
            node.topRight = rec(top_right)
            node.bottomLeft = rec(bottom_left)
            node.bottomRight = rec(bottom_right)

            return node

        return rec(grid)