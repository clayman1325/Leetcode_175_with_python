class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        # if(len(tokens) < 1): return tokens
        # if(len(tokens) < 2): return tokens[0]
        result = []
        for element in tokens:
            if element not in operations.keys():
                result.append(int(element))
            else:
                num2 = result.pop()
                num1 = result.pop()
                operation = operations[element]
                calc = int(operation(int(num1), int(num2)))
                result.append(calc)

        return result[0]