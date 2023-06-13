# Question  14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


def longestCommonPrefix2(self, strs: List[str]) -> str:
    def findCommonLocalPrefix(str1, str2):
        prefix = ""
        idx = 0
        while(
            idx < len(str1) and
            idx < len(str2) and
            str1[idx] == str2[idx]
        ):
            prefix += str1[idx]
            idx += 1

        return prefix

    common_prefix = strs[0]
    for x in range(len(strs) - 1):
        cur_comm_prefix = findCommonLocalPrefix(strs[x], strs[x+1])
        common_prefix = cur_comm_prefix if len(common_prefix) > len(cur_comm_prefix) else common_prefix

    return common_prefix
# Pseudo code:
# Ideas: Divide and conquer evaluation by two strings with two pointers.
#        Traversing the array calculating the common prexing in elements next to each other.
#        Sort by length and start scanning from shortest to longest words
# 	Vertical scaninng (compare by column in all strings)
#        Binary search
#  	Trie


# 	•	For x in range(len(strs)):
# 	•	findCommonPrefix(strs[x], strs[x+1])

# 	•	findCommonprefix(word1, word2, cur_common_prefix)
# 	•	Count = 0
# 	•	X = 0
# 	•	while(match):
# 	•	Word1[x] == word2[x]
# 	•	Count += 1
# 	•	Return min(common_prefix, cur_common_prefix)
# 	•

# Input: strs = ["flower","flow","flight"]
# x= 0
# Max = 0
# 	•	findCommonprefix(flow, flight, 4)
# 	•	Count = 2
# 	•	Match = true
# 	•	X = 2
# 	•
# 


