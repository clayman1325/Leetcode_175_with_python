# Question  205. Isomorphic Strings
# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

#  Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        idx = 0
        str = s.split(' ')

        if(len(pattern) != len(str)):
            return False

        for i in range(len(str)):
            c = pattern[i]
            w = str[i]

            pattern_key  = 'pattern_{}'.format(c)
            s_key = 's_{}'.format(w)

            if(pattern_key not in dic):
                dic[pattern_key] = i

            if(s_key not in dic):
                dic[s_key] = i

            if(dic[pattern_key] != dic[s_key]):
                return False

        return True

# pattern = "abba", s = "dog cat cat dog"

# dict= { a: dog, b: cat}
# Idx = 2
# P   =
# S   =

# Pseudo code:
# Match the words in s to a letterand find if the pattern is fulfilled
