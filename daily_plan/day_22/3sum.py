class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        for base in range(len(nums)-2):
            l = base + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[base] + nums[l] + nums[r]
                if sum == 0:
                    result.add((nums[base],nums[l], nums[r]))
                    while l+1 < len(nums) and nums[l] == nums[l+1]:
                        l += 1
                    while r >=0 and nums[r-1] == nums[r]:
                        r -= 1
                if sum > 0:
                    r -= 1
                else:
                    l += 1

        result = list(result)
        return result