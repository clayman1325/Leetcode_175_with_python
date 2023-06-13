class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        idx = 0
        str = s.split(' ')

        if(len(pattern) != len(str)):
            return False

        for i in range(len(str)):
            p = pattern[i]
            s = str[i]

            p_key = 'p_{}'.format(p)
            s_key = "s_{}".format(s)

            if(p_key not in dic):
                dic[p_key] = s

            if(s_key not in dic):
                dic[s_key] = p

            if(dic[p_key] != s or dic[s_key] != p):
                return False

        return True