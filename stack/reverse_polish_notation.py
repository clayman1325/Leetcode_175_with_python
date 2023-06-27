class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operate(num1, num2, operator):
            result = 0
            num1 = int(num1)
            num2 = int(num2)

            if(operator == "+"):
                result =  num2 + num1
            elif (operator == "-"):
                result =  num2 - num1
            elif (operator == "*"):
                result =  num2 * num1
            else:
                result =  int(num2 // num1)

            return result

        operators = set(["+", "*", "-", "/"])

        stack = []
        for x in tokens:
            print(stack)
            if not operators & set([x]):
                stack.append(int(x))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                num = operate(num1, num2, x)
                print(stack, num1, num2, x)
                stack.append(num)

        return stack.pop()




# tokens = ["2","1","+","3","*"]
# stack = 1 + 2 3
# num.  = 1 + 2 * 3

#  2 + 1 * 3

#  ["4","13","5","/","+"]

#  stack = 4 13 /5


#  4

