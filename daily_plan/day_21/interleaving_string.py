class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = []
        for row in range(len(s1)+1):
            dp.append([False] * (len(s2)+1))

        for row in range(len(s1)+1):
            for col in range(len(s2)+1):
                if row == 0 and col == 0:
                    dp[row][col] = True
                elif row == 0:
                    dp[row][col] = dp[row][col - 1] and s2[col - 1] == s3[row + col - 1]
                elif col == 0:
                    dp[row][col] = dp[row-1][col] and s1[row - 1] == s3[row + col - 1]
                else:
                    a = dp[row-1][col] and s1[row - 1] == s3[row + col - 1]
                    b = dp[row][col - 1] and s2[col - 1] == s3[row + col - 1]
                    dp[row][col] = a or b
        return dp[len(s1)][len(s2)]