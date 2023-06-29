def isPalindrome(self, s: str) -> bool:
    if(len(s) < 1): return False

    s = s.lower()
    palindrome = ""
    for x in s:
        ascii = ord(x)
        word   = ascii < 123 and ascii > 96
        number = ascii < 58  and ascii > 47
        if(word or number):
            palindrome += x

    left = 0
    right = len(palindrome) - 1
    while(left < right):
        if(palindrome[left] != palindrome[right]): return False
        left  += 1
        right -= 1

    return True