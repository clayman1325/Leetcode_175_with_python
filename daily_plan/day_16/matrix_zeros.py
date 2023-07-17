class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zeros.append((row, col))

        for row, col in zeros:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0
        for row, col in zeros:
            for row in range(len(matrix)):
                matrix[row][col] = 0