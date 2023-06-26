    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth =[0] * len(accounts)
        max_wealth = 0
        for customer in range(len(accounts)):
            for bank in range(len(accounts[0])):
                wealth[customer] += accounts[customer][bank]
                max_wealth = max(max_wealth, wealth[customer])

        return max_wealth