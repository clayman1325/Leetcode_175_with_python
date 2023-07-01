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

    # max_sub_array = [4,-1,2,1]
    # max_value = 6
    # cur_value = 1
    # cur_sub_array = [4, -1,2,1,-5,4]

    # [-2,1,-3,4,-1,2,1,-5,4]


    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    # sliding window build subarrays

    # [-2,1,-3,4,-1,2,1,-5,4]


    #  if sum(subarray) < 0
    #    store max and create new sub array.