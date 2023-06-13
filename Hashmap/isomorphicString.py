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
        t_values = t_dict.values()
        s_values = s_dict.values()

        valid_isomorphic = True
        for x in s_values:
            if(x not in t_values):
                valid_isomorphic = False

        return valid_isomorphic
