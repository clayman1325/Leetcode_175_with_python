class Solution:
    def numDecodings(self, s: str) -> int:
        # @lru_cache(maxsize=None)
        def rec(s, options, code, memo):
            if not s:
                options[0] += 1
                return 1
            left = 0
            right = 0
            option_one = ""
            if int(s[0]) != 0:
                option_one = code[int(s[0])]
                left = rec(s[1:], options, code, memo)
                memo[str(s[1:])] = left
            else:
                return 0
            option_two = ""
            if len(s) > 1 and int(s[0]+s[1]) < 27:
                option_two = code[int(s[0]+s[1])]
                right = rec(s[2:], options, code, memo)
                memo[str(s[2:])] = right
            else:
                return 0

            return left + right


        code = {}
        num = 1

        for i in range(65, 91):
            code[num] = chr(i)
            num += 1

        s = list(s)
        options = [0]
        memo = {}
        rec(s, options, code, memo)

        return options[0]