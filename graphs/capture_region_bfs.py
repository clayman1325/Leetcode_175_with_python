class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def capture_region(board):
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if(board[row][col] == 'O'): board[row][col] = 'X'
                    if(board[row][col] == 'E'): board[row][col] = 'O'

        def bfs(board, row, col):
            cell = tuple([row, col])
            q = []
            if(board[row][col] == "O"):
                q.append(cell)
                board[row][col] = "E"
                look_for_region(board, cell, q, directions)

        def look_for_region(board, cell, q, directions):
            while(len(q) > 0):
                cur_cell = q.pop(0)
                for x in directions:
                    row = cur_cell[0] + x[0]
                    col = cur_cell[1] + x[1]
                    if(
                        row >= 0 and col >= 0 and row <= len(board) - 1 and col <= len(board[0]) - 1  and
                        board[row][col] == "O"
                    ):
                        q.append(tuple([row, col]))
                        board[row][col] = "E"

        directions = [[1,0], [0,1], [0,-1], [-1,0]]
        for row in range(0,len(board)):
            for col in [0, len(board[0])-1]:
                bfs(board, row, col)

        for row in [0, len(board)-1]:
            for col in range(0,len(board[0])):
                bfs(board, row, col)

        capture_region(board)