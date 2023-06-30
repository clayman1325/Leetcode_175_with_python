def climbStairs(self, n: int) -> int:
    def recClimbStairs(n, stairs, memo):
        if(stairs == n):
            return 1
        if(stairs > n):
            return 0

        if(memo.get(stairs)):
            return memo[stairs]

        options = recClimbStairs(n, stairs + 1, memo) + recClimbStairs(n, stairs + 2, memo)
        memo[stairs] = options
        return options

    return recClimbStairs(n, 0, {})
