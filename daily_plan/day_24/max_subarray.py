class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = -10000
        cur_value = 0

        for x in nums:
            cur_value += x

            if(max_value < cur_value):
                max_value = cur_value
            if(cur_value < 0):
                cur_value = 0

        return max_value