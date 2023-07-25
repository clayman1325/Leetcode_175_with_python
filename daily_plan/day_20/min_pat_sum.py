class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                prev_values = []
                cur_value = grid[row][col]
                if(row - 1 >= 0):
                    prev_values.append(grid[row-1][col]  + cur_value)
                if(col - 1 >= 0):
                    prev_values.append(grid[row][col-1] + cur_value)

                grid[row][col] = min(prev_values) if prev_values else grid[row][col]
        return grid[len(grid) - 1][len(grid[0]) - 1]