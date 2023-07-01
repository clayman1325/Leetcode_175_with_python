def backspaceCompare(self, s: str, t: str) -> bool:
    def erase(s):
        queue = []
        result = []
        for x in reversed(range(len(s))):
            char = s[x]
            if(char == "#"):
                queue.append("#")
            else:
                if(queue):
                    queue.pop()
                else:
                    result.append(char)
        return result

    s = erase(s)
    t = erase(t)

    return s == t