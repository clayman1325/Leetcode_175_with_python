# Question 1
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Input: prices = [7,6,4,3,1]
# Output: 0
# .

# Input: ([],[])


# /**
# * @param {number[]} prices
# * @return {number}
# */
var maxProfit = function(prices) {
    Max_profit = 0
	min = 0
	max = 0
	Cur_profit = 0

	For i in range(prices):
		if(prices[i] < min):
			Max_profit = max(max_profit, max - min)
			Min = prices[i]
		if(prices[i] > max):
			Max_profit = max(max_profit, max - min)
			Max = prices[i]

	Return max_profit = max(max_profit, max - min)
};

# prices = [7,1,5,3,6,4]
# Min         7 1 1 1 1 1
# Max        7 1 5 3 6 6
# P                  4 2 5 5

# Def maxProfit
	# Max_profit = 0
	# min = 0
	# max = 0
	# Cur_profit = 0

	# For i in range(prices):
	# 	if(prices[i] < min):
	# 		Max_profit = max(max_profit, max - min)
	# 		Min = prices[i]
	# 	if(prices[i] > max):
	# 		Max_profit = max(max_profit, max - min)
	# 		Max = prices[i]

	# Return max_profit = max(max_profit, max - min)




# prices = [7,1,5,3,6,4]
# 	•	Buy when it is cheaper and sell when its costly

# prices = [7,1,5,3,6,4]
#                   B      s        p  = 5
#                      B   s        p  = 1
#                         Bs        p = 3


# prices = [7,6,4,3,1]
#                            0

# PseudoCode.
# 	•	Loop and buy i
# 	•	Loop sell in the next max val
# 	•	Store profit
# 	•	Return max profit
# 