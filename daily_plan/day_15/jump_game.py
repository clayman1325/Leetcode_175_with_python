class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2: return True

        dp = [False] * len(nums)
        dp[len(nums) - 1] = True
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                while(j > 0 and not dp[i]):
                    j -= 1
                    if nums[j] + j > i:
                        dp[i] = True

                if not dp[i]:
                    return False
        return True