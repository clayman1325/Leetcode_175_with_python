class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        price = prices[0]
        for x in range(1, len(prices)):
            if(price > prices[x]):
                price= prices[x]
            else:
                max_profit += prices[x] - price
                price = prices[x]

        return max_profit