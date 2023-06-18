class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        dict = {}
        for x in range(len(nums)):
            dict[(x + k) % len(nums)] = nums[x]
        for x in range(len(nums)):
            nums[x] = dict[x]
        print(nums)