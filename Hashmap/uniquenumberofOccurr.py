# Question 1207. Unique Number of Occurrences
#  Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

# Example 1:

# Input: arr = [1,2,2,1,1,3]
# {1:3, 2,2, 3,1}
# [false, True, True, True]
# Example 2:
# Input: arr = [1,2]

# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict = {}
        for x in arr:
            if(dict.get(x) is not None):
                dict[x] += 1
            else:
                dict[x] = 1

        validate = [False] * (len(arr) + 1)

        for k in dict:
            if(validate[dict[k]]):
                return False
            else:
                validate[dict[k]] = True

        return True

