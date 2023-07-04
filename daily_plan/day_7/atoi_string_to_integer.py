class Solution:
    def myAtoi(self, s: str) -> int:
        limit = 2147483647
        sign = ""

        number = ""
        find_digit = False
        for i in range(len(s)):
            char = s[i]

            if ord(char) < 58 and ord(char) > 47:
                if not find_digit: find_digit = True
                number += char
            else:
                if find_digit:
                    break
            if sign != "" and not find_digit: return 0
            if(not find_digit):
                if char != " " and char != "+" and char != "-": return 0
                if sign != ""  and (char == "+" or char == "-"): return 0
            if i < len(s) - 1 and char == "-" or char == "+": sign = char
        if not find_digit: return 0

        exp = 1
        idx = len(number) - 1
        result = 0
        while(idx >= 0):
            num = int(number[idx]) * exp
            result += num
            idx -= 1
            exp *= 10

        if sign == "-": result *= -1

        result = max(result, -2**31)
        result = min(result, (2**31)-1)

        return result