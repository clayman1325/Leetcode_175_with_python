# Question  202. Happy Number
# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Example 2:

# Input: n = 2
# Output: false
# 4 = 4
# 16 = 16
# 1 + 36= 35
# 9 + 25 = 34
# 9 + 16 = 25



class Solution:
    def isHappy(self, n: int) -> bool:
        def splitNumbers(num, list):
            if(num/10 == 0):
                if(num%10 > 0):
                    list.append(num%10)
                return list

            list.append(num % 10)
            splitNumbers(num//10, list)

        cur_sum = 0
        cycle = {}
        while(cur_sum != 1):
            list1 = []
            splitNumbers(n, list1)
            cur_sum = 0
            for x in list1:
                cur_sum += x ** 2
            n = cur_sum
            if(cycle.get(cur_sum)): return False
            cycle[cur_sum] = cur_sum


        return True

#         Pseudo code:
# Calculate the sum of the squares of the number
# If the sum == 1 return true else store the num in a set and continue looking
# If found a cycle in the hashSet return false
