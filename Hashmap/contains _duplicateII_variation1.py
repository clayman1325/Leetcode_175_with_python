# Question 219. Contains Duplicate II
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Hash = {1:[0,3], 2:1,3:2 }
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# {1:[0,2,3]}
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
# {1:[0,3],2:[1,4],3:[2,5],}



class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        def build_dict(nums, k):
            dict = {}
            for x in range(len(nums)):
                if(nums[x] in dict):
                    if(len(dict[nums[x]]) == 1 and x - dict[nums[x]][0] > k):
                        dict[nums[x]] = [x]
                    elif(len(dict[nums[x]]) == 1):
                        dict[nums[x]].append(x)
                else:
                    dict[nums[x]] = [x]

            return dict

        dict = build_dict(nums, k)

        for x in nums:
            if(len(dict[x]) > 1):
                return True

        return False

# Pseudo code:
# Build a hash with num key and indexes values
# For all key where values are > 1
# See if abs(j-i) < k if so true
# Inf not at the end of the loop return False
