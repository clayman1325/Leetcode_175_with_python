class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = [[], [nums[0]]]
        for idx in range(1, len(nums)):
            num = nums[idx]
            cur_set = [num]
            cur_sets = []
            for s in sets:
                cur_sets.append(cur_set + s)
            sets += cur_sets
        return sets