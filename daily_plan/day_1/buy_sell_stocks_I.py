def maxProfit(self, prices: List[int]) -> int:
    p_buy = prices[0]
    p_sell = prices[0]
    profit = p_buy - p_sell
    for p in prices:
        if(p < p_buy):
            p_buy = p
        profit = max(profit, p - p_buy)
    return profit