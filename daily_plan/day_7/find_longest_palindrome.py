class Solution:
    def longestPalindrome(self, s: str) -> str:
        def find_palindrome(s, l, r, center):
            palindrome = ""
            if center: palindrome = center
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    left = s[l] + palindrome
                    palindrome = left + s[r]
                else:
                    l = -2
                l -= 1
                r += 1
            return palindrome

        if s == "": return s
        start = 0
        max_palindrome = ""
        while start < len(s)-1:
            first = find_palindrome(s, start, start + 1, "")
            second = find_palindrome(s, start-1, start + 1, s[start])

            if len(max_palindrome) < len(first): max_palindrome = first
            if len(max_palindrome) < len(second): max_palindrome = second
            start += 1
        if max_palindrome == "": return s[0]
        return max_palindrome