# Question  1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# targe[[[t = 9
# [2,7,11,15],
# 92
# [3,2,95,4,-3]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for x in range(len(nums)):
            candidate = target - nums[x]
            s[candidate] = x

        for x in range(len(nums)):
            if(s.get(nums[x])):
                if(s.get(nums[x]) != x):
                    return [s.get(nums[x]), x]


# Pseudo code:
# Build hash of key target - num and value idx in the nums array
# Transverse array and find if hash key if the current value exist that means some value needs this value to meet target.
