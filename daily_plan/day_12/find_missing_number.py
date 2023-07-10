class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dict = Counter(nums)
        for num in range(len(nums)+1):
            if dict[num] < 1:
                return num
    def missingNumber2(self, nums: List[int]) -> int:
        length = len(nums)
        total  = 0
        for num in range(1, length + 1):
            total += num
        sum = 0
        for i in range(length):
            sum += nums[i]
        return total - sum