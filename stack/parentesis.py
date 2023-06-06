class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s) == 1): return False

        parentesis = {
            "]":"[",
            "}":"{",
            ")":"("
        }

        stack = []

        for x in s:
            if x in parentesis:
                last_element = stack.pop() if stack else "#a"
                if(parentesis[x] != last_element):
                    return False
            else:
                stack.append(x)

        if(len(stack) > 0): return False

        return True