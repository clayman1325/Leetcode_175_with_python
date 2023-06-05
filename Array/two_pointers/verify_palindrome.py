class Solution:
    def isPalindrome(self, s: str) -> bool:
        if(len(s) == 0): return True
        if(len(s) == 1): return True

        chars = []

        for letter in s:
            # char_ascii = ord(letter)
            # if(char_ascii <= 90  and char_ascii >= 65 or char_ascii <= 122 and char_ascii >= 97 or
            #    char_ascii <= 57  and char_ascii >= 48
            # ):
            if(letter.isalnum()):
                chars.append(letter.lower())

        if(len(chars) == 0): return True
        if(len(chars) == 2): return chars[0] == chars[1]

        left = 0
        right = len(chars) - 1

        while(left < right):
            if(chars[left] != chars[right]):
                return False
            left  += 1
            right -= 1

        return True