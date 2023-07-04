class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = 1
        color = 0
        while(r < len(nums)):
            if(nums[l] != color and nums[r] == color):
                aux = nums[l]
                nums[l] = nums[r]
                nums[r] = aux
            if nums[l] == color:
                l += 1
                r = l
            r += 1
        r = l + 1
        color = 1
        while(r < len(nums)):
            if(nums[l] != color and nums[r] == color):
                aux = nums[l]
                nums[l] = nums[r]
                nums[r] = aux
            if nums[l] == color:
                l += 1
                r = l
            r += 1
        print(nums)