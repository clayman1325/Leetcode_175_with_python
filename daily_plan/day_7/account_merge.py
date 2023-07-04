class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def dfs(merge_account, email, visited, adj):
            if(not adj.get(email)): return
            visited.add(email)
            merge_account.append(email)

            for next_email in adj[email]:
                if(next_email not in visited):
                    dfs(merge_account, next_email, visited, adj)

        visited = set([])
        adj = {}

        for account in accounts:
            account_size = len(account)
            account_first_email = account[1]
            if(account_size == 2): adj[account_first_email] = [account_first_email]
            for idx in range(2, account_size):
                account_email = account[idx]
                if(not adj.get(account_first_email)):
                    adj[account_first_email] = [account_first_email]
                adj[account_first_email].append(account_email)
                if(not adj.get(account_email)):
                    adj[account_email] = [account_email]
                adj[account_email].append(account_first_email)
        result = []
        for account in accounts:
            account_name = account[0]
            account_fist_email = account[1]
            if(account_fist_email not in visited):
                merge_account = []
                dfs(merge_account, account_fist_email, visited, adj)
                merge_account.sort()
                result.append([account_name] + merge_account)
        return result