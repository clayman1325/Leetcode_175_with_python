class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(heights, row, col, visited, memo):
            if memo.get((row,col)): return memo[(row,col)]
            if col == -1 or row == -1: return "p"
            if col == len(heights[0]) or row == len(heights): return "a"

            directions = [[1,0],[0,1],[-1,0], [0,-1]]

            result = ""
            for dir in directions:
                next_row = row + dir[0]
                next_col = col + dir[1]

                cell = False
                if next_row == -1 or next_row == len(heights) or next_col == -1 or next_col == len(heights[0]):
                    cell = dfs(heights, next_row, next_col, visited,  memo)
                elif(
                    (next_row, next_col) not in visited and
                    next_row > -1 and next_row < len(heights) and next_col > -1 and next_col < len(heights[0]) and
                    heights[row][col] >= heights[next_row][next_col]
                ):
                    visited.add((next_row, next_col))
                    cell = dfs(heights, next_row, next_col, visited, memo)

                if(cell):
                    if("p" in cell and "a" in cell):
                        memo[(row,col)] = cell
                        return cell
                    result += cell + " "

            return result
        result = []
        memo = {}
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                visited = set()
                visited.add((row, col))

                cell = dfs(heights, row, col, visited, memo)
                print((row, col), cell)

                if("p" in cell and "a" in cell): result.append([row, col])

        return result