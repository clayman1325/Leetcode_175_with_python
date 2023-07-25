class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1: return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        grid = obstacleGrid
        grid[0][0] = 1
        start = 0
        for col in range(1, n):
            if grid[0][col] == 1:
                grid[0][col] = 0
            else:
                grid[0][col] = grid[0][col -1]
        for row in range(1,m):
            for col in range( n):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                else:
                    left = grid[row][col-1] if col -1 >= 0 else 0
                    up = grid[row-1][col]
                    grid[row][col] = up + left
        return grid[m-1][n-1]