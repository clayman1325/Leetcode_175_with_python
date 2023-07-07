class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]

        max_product = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            cur_val = max(num, cur_max * num, cur_min * num)
            cur_min = min(num, cur_max * num, cur_min * num)
            cur_max = cur_val

            max_product = max(max_product, cur_max)

        return max_product