class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum = 0
        dict = {0:1}
        for num in nums:
            sum += num
            if dict.get(sum - k):
                count += dict[sum-k]
            if dict.get(sum):
                dict[sum] += 1
            else:
                dict[sum] = 1
        return count