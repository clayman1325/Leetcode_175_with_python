def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    dict = {}
    for x in magazine:
        if(dict.get(x)):
            dict[x] += 1
        else:
            dict[x] = 1

    for x in ransomNote:
        if(not dict.get(x)): return False
        dict[x] -= 1

    return True