class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(target > nums[len(nums) - 1]): return len(nums)
        if(target < nums[0]): return 0
        left = 0
        right = len(nums) - 1

        while(left <= right):
            idx = left + (right - left) // 2

            if(nums[idx] == target):
                return idx

            if(target > nums[idx]):
                left = idx + 1
            else:
                right = idx - 1

        return left