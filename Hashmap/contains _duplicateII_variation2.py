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



def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    dict = {}
    for x in range(len(nums)):
        if(nums[x] in dict):
            return True
        else:
            dict[nums[x]] = x
        if(x >= k):
            dict.pop(nums[x - k])

    return False

# Pseudo code:
# Build a hash with num key and indexes values
# For all key where values are > 1
# See if abs(j-i) < k if so true
# Inf not at the end of the loop return False
