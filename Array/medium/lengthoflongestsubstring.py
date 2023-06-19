class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		if(len(s) < 1): return 0

		left = 0
		right = 0
		max_count = 0
		count = 0
		queue = []
		while(right < len(s)):
			if(s[right] not in queue):
				queue.append(s[right])
				count += 1
				right += 1
			else:
				max_count = max(max_count, count)
				popped = queue.pop(0)
				count -=1
				left += 1
				while(popped != s[right]):
					count -=1
					left += 1
					popped = queue.pop(0)
		max_count = max(max_count, count)
		return max_count