class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        limit = len(nums)
        left  = 0
        right = 0
        while(right < limit):
            if(right+1 < len(nums) and nums[right] != nums[right+1]):
                nums[left] = nums[right]
                left += 1
            right += 1

        nums[left] = nums[len(nums) - 1]

        return left + 1