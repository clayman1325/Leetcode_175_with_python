class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        def buildDict(word) -> dict:
            dict = {}
            for char in word:
                if char not in dict:
                    dict[char]  = 1
                else:
                    dict[char] = dict[char] + 1

            return dict

        ranDict = buildDict(ransomNote)
        magDict = buildDict(magazine)

        for char in ransomNote:
            ranCount = ranDict[char]

            if(char not in magDict.keys() or magDict[char] < ranDict[char]):
                return False

        return True