class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 1: return [[""]]

        sorted = []
        for str in strs:
            lst_str = list(str)
            lst_str.sort()
            sorted.append(" ".join(lst_str))

        dict = {}
        for i in range(len(sorted)):
            str = sorted[i]
            if dict.get(str):
                dict[str].append(i)
            else:
                dict[str] = [i]

        result = []
        for values in dict.values():
            group = []
            for value in values:
                group.append(strs[value])
            result.append(group)

        return result