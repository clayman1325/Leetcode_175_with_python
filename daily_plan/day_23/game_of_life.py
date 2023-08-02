
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def calculate_next_state(row, col, board):
            count = 0
            neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
            for neigh in neighbors:
                next_row = row + neigh[0]
                next_col = col + neigh[1]
                if next_row >= 0 and next_row < len(board) and next_col >=0 and next_col < len(board[0]):
                    if board[next_row][next_col] == 1 or board[next_row][next_col] == "0":
                        count += 1

            if board[row][col] == 1 or board[row][col] == "0":
                if count < 2 or count > 3:
                    return "0"
                elif count == 2 or count == 3:
                    return 1
            else:
                if count == 3:
                    return "1"
                else:
                    return 0

        m = len(board)
        n = len(board[0])

        change = { "0": 0, "1": 1, 0:0, 1:1}
        for i in range(m):
            for j in range(n):
                board[i][j] = calculate_next_state(i, j, board)
        for i in range(m):
            for j in range(n):
                board[i][j] = change[board[i][j]]

