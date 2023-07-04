class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def dfs(nums, length, target):
            if(target == 0): return True
            if(target < 0 or length == 0): return False
            result = dfs(nums, length -1, target - nums[length-1]) or dfs(nums, length -1, target)

            return result
        total_sum = sum(nums)
        if total_sum % 2 != 0: return False
        target = total_sum // 2
        return dfs(tuple(nums), len(nums) - 1, target)