class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(board, visited, word, length, row, col):
            if(length == len(word)): return True

            directions = [[1,0],[0,1],[-1,0],[0,-1]]

            visited.add((row, col))

            for dir in directions:
                next_row = row + dir[0]
                next_col = col + dir[1]

                if(
                    next_row >= 0 and col >= 0 and next_row < len(board) and next_col < len(board[0]) and
                    (next_row, next_col) not in visited
                ):
                    char = word[length]

                    if char == board[next_row][next_col]:
                        result = search(board, visited, word, length + 1, row + dir[0], col + dir[1])
                        if result: return True

            return False

        visited = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                char = board[row][col]

                if char == word[0] and (row, col) not in visited:
                    visited = set()
                    result = search(board, visited, word, 1, row, col)
                    if result: return True


        return False