def isAnagram(self, s: str, t: str) -> bool:
    anagram = {}
    for ch in s:
        if(anagram.get(ch)):
            anagram[ch] += 1
        else:
            anagram[ch] = 1

    for x in t:
        if(anagram.get(x)):
            anagram[x] -= 1
            if anagram[x] < 0: return False
        else:
            return False

    for x in anagram.keys():
        if(anagram[x] > 0): return False

    return True