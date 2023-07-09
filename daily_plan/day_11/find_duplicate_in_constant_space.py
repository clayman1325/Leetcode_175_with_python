class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = 1
        r = len(nums) - 1
        while l <= r:
            num = (l + r) // 2

            count = 0
            for n in range(len(nums)):
                if nums[n] <= num: count += 1

            if count > num:
                duplicate = num
                r = num - 1
            else:
                l = num + 1

        return duplicate