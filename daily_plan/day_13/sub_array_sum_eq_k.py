class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total_sum = []
        sum = 0
        for num in nums:
            sum += num
            total_sum.append(sum)
        count = 0
        cur_sum = 0
        for i in range(len(nums)):
            if nums[i] == k: count += 1
            for j in range(i+1,len(nums)):
                prev_sum = 0 if i == 0 else total_sum[i-1]
                cur_sum = total_sum[j] - prev_sum
                if cur_sum == k: count += 1

        return count