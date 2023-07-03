class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if(len(nums) == 1): return 0 if target == nums[0] else -1
        nums_len = len(nums)
        min_value = 10000
        min_idx = 0
        for x in range(len(nums)):
            if(min_value > nums[x]):
                min_value = nums[x]
                min_idx = x

        idx = min_idx
        print(min_idx, len(nums))
        while(idx < min_idx + len(nums)):
            print("..", idx % nums_len)
            cur_idx = idx if min_idx == 0 else (idx % nums_len)
            if(nums[cur_idx] == target): return cur_idx
            idx += 1

        return -1