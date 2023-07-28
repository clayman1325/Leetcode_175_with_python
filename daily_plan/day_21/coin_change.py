class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [100000] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for val in range(coin, amount + 1):
                dp[val] = min(dp[val], dp[val - coin] + 1)
        return dp[amount] if dp[amount] != 100000 else - 1
# dp = [0,1,2,3,4,1,6,7,8,8,10,11,12]
#     #   1 2 3 4 5 6 7 8 9 10 11
#     # 1 1 0 1 0 0 1 0 1 0 0  1
#     # 2 0 1 1 2 0 0 1 1 2 0  0
    # 5 0 0 0 0 1 1 1 1 1 2  2