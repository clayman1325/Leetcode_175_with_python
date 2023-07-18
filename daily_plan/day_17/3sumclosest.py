class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = nums[0] + nums[1] + nums[len(nums) - 1]
        min_diff = 10000
        pivot = 0
        nums.sort()
        while pivot < len(nums)-2:
                left = pivot + 1
                right = len(nums) - 1
                while left < right:
                        sum = nums[pivot] + nums[left] + nums[right]
                        diff = target - sum
                        if min_diff > abs(diff):
                                min_diff = abs(diff)
                                result = sum

                        if diff == 0: return result

                        if(diff < 0):
                                right -= 1
                        else:
                                left += 1
                pivot += 1
        return result