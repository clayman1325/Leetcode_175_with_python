class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 1: return int(s[0])
        operators = set(["+","-", "*","/"])
        operations = {
            "+": lambda a, b :  a+b,
            "-": lambda a, b :  a-b,
            "*": lambda a, b :  a*b,
            "/": lambda a, b :  a//b,
        }

        stack = []
        pre = ""
        for i in range(len(s)):
            if s[i] != " ":
                if s[i] in operators:
                    stack.append(s[i])
                    pre = ""
                elif i + 1 < len(s) and s[i+1] not in operators and s[i+1] != " ":
                    pre += s[i]
                else:
                    print(s[i])
                    pre += s[i]
                    stack.append(pre)
                    pre = ""

        if pre != "":
            stack.append(pre)
        num_1 = None
        num_2 = None
        operator = ""
        result = 0

        while stack:
            element = stack.pop()

            if num_1 is None:
                num_1 = element
            elif operator == "":
                operator = element
            else:
                num_2 = element
            if num_1 != None and num_2 != None:
                run = operations[operator]
                eval = run(int(num_2), int(num_1))
                result = eval
                stack.append(eval)
                num_1 = None
                num_2 = None
                operator = ""

        if num_1 and result == 0:
            result = int(num_1)
        return result