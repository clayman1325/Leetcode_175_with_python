class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
      """
      Do not return anything, modify nums in-place instead.
      """
      l = 0
      r = 1
      lenght = len(nums)
      while(r < lenght):
        if nums[l] != 0:
          l += 1
          if r == l:
            r += 1
        elif nums[r] != 0:
          aux = nums[l]
          nums[l] = nums[r]
          nums[r] = aux
          l += 1
          r += 1
        else:
          r += 1