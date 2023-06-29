def isValid(self, s: str) -> bool:
    if(len(s)<2): return False

    brackets = {
        "]": "[",
        "}": "{",
        ")": "("
    }
    stack = []
    s = list(s)

    for x in s:
        if(x not in brackets):
            stack.append(x)
        else:
            if(len(stack) < 1): stack.append("$")
            last_elem = stack.pop()
            if(last_elem != brackets.get(x)): return False

    return len(stack) == 0