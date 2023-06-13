# Question 58. Length of Last Word

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal  substring consisting of non-space characters only.
# Input: ([],[])

# Input: s = "Hello World"
# Output: 5

# Input: s = "   fly me   to   the moon  "
# Output: 4

# Input: s = "luffy is still joyboy"
# Output: 6



# Def lengthOfLastWord(s):
#        s   = list(s)
#         idx = len(s) - 1
#         for x in range(len(s) - 1, -1, -1):
#             if(s[x] != ' '):
#                 idx = x
#                 break
#         count = 0
#         for x in range(idx, -1, -1):
#             if(s[x] != ' '):
#                 count += 1
#             else:
#                 break

#         return count

# 
# Pseudo code
# 0.	Convert s to array
# 	•	Loop from end to beginning and find the first none space word.
# 	•	For x in range(s) - 1, 0, -1:
# 	•	Once find the firs char count backwards until find another space

# 


