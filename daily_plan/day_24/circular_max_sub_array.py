class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = -10000
        sum = [nums[0]]
        for i in range(1,len(nums)):
            sum.append(nums[i-1] + nums[i])
        print(sum)
        sum = []
        i = len(nums) // 2
        sum = [nums[i]]
        for c in range(1, len(nums)):
            idx = (i) % len(nums)
            sum.append(nums[idx-1] + nums[idx])
            i += 1

        i = 0
        count = 0
        cur_sum = 0
        while count < len(nums):
            idx = (i) % len(nums)
            if cur_sum < 0:
                cur_sum = nums[idx]
            else:
                cur_sum += nums[idx]
            cur_sum = max(cur_sum, nums[idx])
            max_sum = max(max_sum, cur_sum)

            i += 1
            count += 1

        i = len(nums) // 2
        count = 0
        cur_sum = 0
        while count < len(nums):
            idx = (i) % len(nums)
            print(nums[idx])
            if cur_sum < 0:
                cur_sum = nums[idx]
            else:
                cur_sum += nums[idx]
            cur_sum = max(cur_sum, nums[idx])
            max_sum = max(max_sum, cur_sum)

            i += 1
            count += 1
        return max_sum
