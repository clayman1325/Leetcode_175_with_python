class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 1 and len(matrix[0]) == 1: return int(matrix[0][0])
        if len(matrix) == 1: return int(max(matrix[0]))

        dp = []
        for i in range(len(matrix)):
            cols = [0] * len(matrix[0])
            dp.append(cols)
        for j in range(len(matrix[0])):
            dp[0][j] = int(matrix[0][j])
        max_square = int(max(matrix[0]))
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    if j == 0:
                        past_values = 0
                    else:
                        past_values = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    dp[i][j] = past_values + 1

                max_square = max(max_square, dp[i][j])

        return max_square * max_square