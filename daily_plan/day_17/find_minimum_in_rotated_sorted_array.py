class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            target = nums[mid]
            if target < nums[mid-1]: return target

            if target > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]

