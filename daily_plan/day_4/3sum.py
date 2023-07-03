class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for l in range(len(nums)):
            m = l + 1
            r = len(nums) - 1
            target = nums[l]
            while(m < r):
                if(nums[m] + nums[r] + nums[l] == 0):
                    cur_result = [nums[l], nums[m], nums[r]]
                    result.append(cur_result)
                    m += 1
                    r -= 1
                    while m < r and nums[m] == nums[m - 1]:
                        m += 1

                if(nums[m] + nums[r] + nums[l] > 0):
                    r -= 1
                else:
                    m += 1

        return result