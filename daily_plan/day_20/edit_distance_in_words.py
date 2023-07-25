class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0: return len(word2)
        if len(word2) == 0: return len(word1)

        dp = []
        for row in range(len(word1)+1):
                dp.append([0] * (len(word2)+1))
        for col in range(1,len(word2)+1):
                dp[0][col] = dp[0][col-1] + 1
        for row in range(1,len(word1)+1):
                dp[row][0] = dp[row-1][0] + 1
        for row in range(1,len(word1)+1):
                for col in range(1,len(word2)+1):
                        diag = dp[row-1][col-1]
                        if word2[col-1] == word1[row-1]:
                                dp[row][col] = diag
                        else:
                                up = dp[row-1][col]
                                left = dp[row][col-1]
                                dp[row][col] = min(up, min(left, diag)) + 1
        return dp[len(word1)][len(word2)]