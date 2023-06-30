class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict = {}

        for x in s:
            if(dict.get(x)):
                dict[x] += 1
            else:
                dict[x] = 1

        odd = 0
        for x in dict:
            if(dict[x] % 2 != 0):
                odd += 1

        result = 0
        for x in dict:
            if(dict[x] % 2 == 0):
                result += dict[x]
            else:
                result += dict[x] - 1

        if(odd > 0): result += 1

        return result