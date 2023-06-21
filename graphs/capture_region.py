class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def look_for_region(board, cell, visited, directions, region):
            for dir in directions:
                row = cell[0] + dir[0]
                col = cell[1] + dir[1]
                if(
                    row > 0 and col > 0 and row < len(board) - 1 and col < len(board[0]) - 1  and
                    board[row][col] == "O" and  tuple([row,col]) not in visited
                ):
                    cell = tuple([row,col])
                    region.append(cell)
                    visited[cell] = True
                    look_for_region(board, cell, visited, directions, region)

        def capture_region(board, region):
            for x in region:
                if(x[0] == "O" or x[0] == len(board) - 1 or x[1] == 0 or x[1] == len(board[0]) - 1):
                    return False

            for cell in region:
                board[cell[0]][cell[1]] = "X"

        directions = [[1,0], [0,1], [0,-1], [-1,0]]
        visited = {}
        for row in range(1,len(board)-1):
            for col in range(1,len(board[0])-1):
                cell = tuple([row, col])
                if(cell not in visited and board[row][col] == "O"):
                    visited[cell] = True
                    region = []
                    region.append(cell)
                    look_for_region(board, cell, visited, directions, region)
                    capture_region(board, region)