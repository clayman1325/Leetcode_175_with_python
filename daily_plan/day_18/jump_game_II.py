class Solution:
    def jump1(self, nums: List[int]) -> int:
        count = 0
        cur_max = 0
        max_idx = 0

        for i in range(len(nums)-1):
            max_idx = max(max_idx, i+nums[i])

            if i == cur_max:
                count += 1
                cur_max = max_idx

        return count