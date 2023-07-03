class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(k,n,idx,cur_sum, cur, result):
            if(len(cur) == k and cur_sum == n):
                result.append(cur)
                return
            if(cur_sum > n or len(cur) > k):
                return
            max = min(n,9)
            for next_id in range(idx + 1, max+1):
                next_cur = [next_id] + cur
                backtrack(k,n,next_id, cur_sum + next_id, next_cur, result)

        result = []
        max = min(n,9)
        for next_id in range(1, max+1):
            backtrack(k,n, next_id, next_id, [next_id], result)
        return result