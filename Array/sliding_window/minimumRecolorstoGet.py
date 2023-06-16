# Question 2379. Minimum Recolors to Get K Consecutive Black Blocks
# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

# You are also given an integer k, which is the desired number of consecutive black blocks.

# In one operation, you can recolor a white block such that it becomes a black block.

# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

# Input: blocks = "WBBWWBBWBW", k = 7
# Output: 3

# Input: blocks = "WBWBBBW", k = 2
# Output: 0



class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        r = 0
        count_w = 0
        min_count = 10000
        while(r < k):
            if(blocks[r] == "W"):
                count_w += 1
            r += 1
        min_count = min(min_count, count_w)
        while(r < len(blocks)):
            if(blocks[r] == "W"):
                count_w += 1
            if(blocks[l] == "W"):
                count_w -= 1
            min_count = min(min_count, count_w)
            l += 1
            r += 1

        return min_count

