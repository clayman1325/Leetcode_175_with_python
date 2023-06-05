class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid_row(board, row, col, num):
            for j in range(col, len(board[0])):
                if(board[row][j] == num):
                    return False

            return True

        def valid_col(board, row, col, num):
            for i in range(row,len(board)):
                if(board[i][col] == num):
                    return False

            return True

        def valid_box(board, row, col, num):
            if(row < 3):
                row_limit = 2
            elif(row < 6 and row > 2):
                row_limit = 5
            else:
                row_limit = 8
            if(col < 3):
                col_limit = 2
            elif(col < 6 and col > 2):
                col_limit = 5
            else:
                col_limit = 8

            for i in range(row_limit - 2, row_limit + 1):
                for j in range(col_limit - 2, col_limit + 1):
                    if(i != row and j != col and board[i][j] == num):
                        return False

            return True

        for row in range(len(board)):
            for col in range(len(board[0])):
                cur_num = board[row][col]
                if(not cur_num == "."):
                    v_row = valid_row(board, row, col + 1, cur_num)
                    v_col = valid_col(board, row + 1, col, cur_num)
                    v_box = valid_box(board, row, col, cur_num)

                    if(not (v_row and v_col and v_box)):
                        return False

        return True