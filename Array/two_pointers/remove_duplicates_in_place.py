class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        limit = len(nums)
        left  = 0
        right = 0
        while(right < limit):
            if(left+1 < len(nums) and nums[left] == nums[left+1]):
                y = left+1
                while(y < limit - 1):
                    nums[y] = nums[y+1]
                    y += 1
            else:
                left += 1

            right += 1

        return left + 1