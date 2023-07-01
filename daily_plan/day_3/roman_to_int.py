class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,

        }
        special_char = ["IV","IX","XL","XC","CD","CM"]
        result = 0
        x = 0
        while x < len(s) - 1:
            if s[x] + s[x+1] in special_char:
                num = dict[s[x] + s[x+1]]
                x += 1
            else:
                num = dict[s[x]]
            result += num
            x += 1

        x = len(s) - 1
        if s[x - 1] + s[x] not in special_char:
            num = dict[s[x]]
            result += num

        return result