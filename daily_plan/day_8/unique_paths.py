class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if(m == 1 or n == 1):
            return 1

        dp = []
        first_row = [1] * (n)
        dp.append(first_row)
        row = [0] * (n)
        for i in range(m - 1):
            dp.append(row)

        for i in range(m):
            for j in range(n):
                if(j == 0):
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]