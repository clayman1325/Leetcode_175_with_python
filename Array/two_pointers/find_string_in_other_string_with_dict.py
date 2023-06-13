# Question  28. Find the Index of the First Occurrence in a String

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def recSearch(idx, needle, dict):
            if(idx >= len(needle)): return -1
            cur_idx = dict.get(needle[idx])[0] if dict.get(needle[idx]) else  -1
            for x in range(idx, len(needle)):
                char = needle[x]

                if(dict.get(char)):
                    candidates = dict.get(char)
                    for y in range(len(candidates)):
                        if(abs(cur_idx - candidates[y]) > 1):
                            recSearch(idx+1, needle, dict)
                        else:
                            cur_idx = candidates[y]
                else:
                    return -1

            return cur_idx - len(needle) + 1

        dict = {}
        for x in range(len(haystack)):
            char = haystack[x]
            if(dict.get(char)):
                dict[char].append(x)
            else:
                dict[char] = [x]


        return recSearch(0, needle, dict);

# Example 1:


# haystack = "sadbutsad", needle = "sad"


# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

# Def strStr(haystack, needle):
# 	Pointer_h = 0
# 	Pointer_n = 0

# 	while(pointer_h < len(h) and pointer_n < len(n)):
# 		if(h[pointer_h] == n[pointer_n]):
# 			Pointer_n += 1
# 		Else:
# 			Pointer_n = 0

# 		Pointer_h += 1
# 	if(pointer_n == len(n) - 1 return True

# 	Return False

# Input:
# h = "leetcode",
#         |
# n = "leeto"
#        |

# 

# Two pointers
# Set pinter h and pinter n to the begiing of the words

# Point_h = 0
# Point_n = 0

# 	•	Move point_h h[p_h] == n[p_n]
# 	•	When find the first letter move both pointers
# 	•	If pointer_n == len(pointer_n) return true
# 	•	Else if  h[p_h] != n[p_n]
# 	•	Return p_n to 0 and continue searching


# Sliding window.
# Create a window of len(n) and move until find the right match

# Rabin-Karp Algorithm (Single Hash)