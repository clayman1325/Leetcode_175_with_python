class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(grid, row, col, directions, visited):
            q = [(row, col)]
            while(q):
                cell = q.pop()
                for dir in directions:
                    row = cell[0] + dir[0]
                    col = cell[1] + dir[1]
                    if(
                        not visited.get(f'{row}-{col}') and
                        row >= 0 and row < len(grid) and col >=0 and col < len(grid[0]) and
                        grid[row][col] == "1"
                    ):
                        visited[f'{row}-{col}'] = True
                        q.append((row, col))



        directions = [[1,0], [-1,0],[0,-1], [0,1]]
        visited = {}
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(not visited.get(f'{row}-{col}') and grid[row][col] == "1"):
                    visited[f'{row}-{col}'] = True
                    bfs(grid, row, col, directions, visited)
                    count += 1

        return count