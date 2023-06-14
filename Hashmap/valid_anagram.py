# Question  242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#  T is form from s

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def build_dict(str):
            dict = {}
            for x in str:
                if(dict.get(x)):
                    dict[x] += 1
                else:
                    dict[x] = 1
            return dict

        if(len(s) != len(t)): return False

        s_dict = build_dict(s)


        for x in t:
            if(s_dict.get(x) and s_dict.get(x) > 0):
                s_dict[x] -= 1
            else:
                return False
        return True

# S_dict = {
# A:0 ,
# N:0
# G:0,
# R:0
# m:0
# }
# Nagaram
#             |

# Pseudo code:
# Build hash of s
# Transverse t and remove -1 each time a letter is found
# if(any of the s letters values is less than 0 or t leeter is not found in s dict return False other wise return Trie
