class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        l_rows = len(grid)
        l_cols = len(grid[0])

        for row in range((l_rows)):
            for col in range((l_cols)):
                if grid[row][col] == "*":
                    start = (row, col)
                    break

        if not start: return -1

        directions = [[1,0], [0,1], [-1,0],[0,-1]]
        q = [[start, 0]]
        visited = set()

        while q:
            cur_pos = q.pop(0)
            row = cur_pos[0][0]
            col = cur_pos[0][1]
            cur_count = cur_pos[1]
            visited.add((row, col))

            if grid[row][col] ==  "#": return cur_count

            for dir in directions:
                next_row = row + dir[0]
                next_col = col + dir[1]

                if(
                    next_row >=0 and next_row < l_rows and next_col >= 0 and next_col < l_cols and
                    grid[next_row][next_col] != "X" and (next_row, next_col) not in visited
                ):
                    visited.add((row, col))
                    q.append([(next_row, next_col), cur_count + 1])

        return -1
