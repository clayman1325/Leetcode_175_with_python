# Question 9. Palindrome Number
# Given an integer x, return true if x is a
# palindrome
# , and false otherwise.


# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.




class Solution:
    def isPalindrome2(self, x: int) -> bool:
        def recDivide(num):
            if((num // 10) == 0):
                return [num, 1]
            recursion = recDivide(num//10)

            return [num%10 * 10 ** recursion[1] + recursion[0], recursion[1] + 1]

        if(x < 0): return False

        return recDivide(x)[0] == x

    def isPalindrome(self, x: int) -> bool:
        if(x < 0): return False

        reverse_number = 0
        y = x
        n = 0
        while(y > 0):
            y //= 10
            n += 1
        n = n //2
        m = n

        reverse_number = x % (10 ** n)

        y = 0
        while(m >0):
            x //= 10
            m -= 1
        n -= 1
        m = 1

        while(n >= 0):
            y = y + reverse_number % 10 * 10 ** n
            reverse_number //= 10
            n -= 1
            m += 1

        return y == x

