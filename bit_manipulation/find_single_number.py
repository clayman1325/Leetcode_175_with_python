class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        accu = nums[0]
        for x in range(1, len(nums)):
            accu = accu ^ nums[x]

        return accu