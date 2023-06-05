class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        curSubArrSum = 0
        result = 10000000

        for right in range(0, len(nums)):
            curSubArrSum += nums[right]

            while curSubArrSum >= target:
                result = min(result, right - left + 1)
                curSubArrSum -= nums[left]
                left += 1

        if(result == 10000000):
            result = 0

        return result