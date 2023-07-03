class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if(len(nums) == 1): return 0 if target == nums[0] else -1
        nums_len = len(nums)
        min_value = 10000
        min_idx = 0
        for x in range(len(nums)):
            if(min_value > nums[x]):
                min_value = nums[x]
                min_idx = x

        idx = min_idx
        l = idx
        r = (idx + len(nums)-1)

        while(l <= r):
            mid = l + (r - l) // 2

            mid_adjusted = mid if min_idx == 0 else (mid % nums_len)

            element = nums[mid_adjusted]

            if element == target: return mid_adjusted

            if(element > target):
                r = mid - 1
            else:
                l = mid + 1

        return -1