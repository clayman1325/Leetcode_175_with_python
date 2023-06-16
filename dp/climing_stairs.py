# Question 70. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# def mySqrt(self, x: int) -> int:
# 	def climbStairs(self, n: int) -> int:
# 		Def top_down(n, memo):
# 			if(Memo[n]): return memo[n]
# 			if(n == 0):
# 				Return [1, memo]
# 			if(n<0):
# 				Return [0, memo]

# 			one = top_down(n -1, memo):
# 			two = top_down(n - 2, memo):
# 			Memo[n] = one[0] + two[0]
# 			Return [Memo[n], memo]
# 		Return top_down(n, {})[0]
	def c2limbStairs(self, n: int) -> int:
		def top_down(n, memo):
			if(memo.get(n)): return memo[n]
			if(n == 0): return 1
			if(n<0): return 0

			one = top_down(n - 1, memo)
			two = top_down(n - 2, memo)

			memo[n] = one + two
			return memo[n]
		memo = {}
		return top_down(n, memo)

	def climbStairs(self, n: int) -> int:
		if(n == 1): return 1
		lst = [1] * n
		lst[1] = 2
		if(n<2): return lst[n]

		for x in range(n - 2):
			x += 2
			lst[x] = lst[x - 2] + lst[x - 1]

		return lst[n-1]