class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def buildDict(str):
            array = list(str)
            dict = {}
            for x in range(len(array)):
                if(dict.get(array[x])):
                    dict[array[x]].append(x)
                else:
                    dict[array[x]] = [x]
            return dict

        s_dict = buildDict(s)
        t_dict = buildDict(t)

        for x in range(len(s)):
            char_s = s[x]
            char_t = t[x]

            if(s_dict[char_s] != t_dict[char_t]): return False

        return True