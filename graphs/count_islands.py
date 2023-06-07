class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def recSearch(grid, row, col, directions):
            if(
                row > len(grid) - 1    or row < 0 or
                col > len(grid[0]) - 1 or col < 0 or
                "0" in grid[row][col]
            ):
                return

            grid[row][col] = "0"

            recSearch(grid, row + directions[0][0], col + directions[0][1], directions)
            recSearch(grid, row + directions[1][0], col + directions[1][1], directions)
            recSearch(grid, row + directions[2][0], col + directions[2][1], directions)
            recSearch(grid, row + directions[3][0], col + directions[3][1], directions)

        directions = [[1,0], [-1,0],[0,-1], [0,1]]
        total = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if("1" in grid[row][col]):
                    recSearch(grid, row, col, directions)
                    total += 1

        return total