class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def build(open, close, option, options):
            if open == 0 and close == 0:
                options.append(option)
                return

            if open > 0:     build(open - 1, close, option + "(", options)
            if open < close: build(open, close - 1, option + ")", options)

        options =[]
        build(n, n, "", options)

        return options


