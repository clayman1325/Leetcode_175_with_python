class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = list(str(x))
        l = 0
        r = len(num) - 1
        lenght = len(num)

        while(l < r):
            if num[l] != num[r]: return False
            l += 1
            r -= 1

        return True