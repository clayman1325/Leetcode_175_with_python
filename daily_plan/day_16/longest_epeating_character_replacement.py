class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def calculate_change(s, k, mid):
            max_count = 0
            left = 0
            right = 0
            dict = {}
            while right < len(s):
                dict[s[right]] = dict.get(s[right], 0) + 1

                if right - left + 1 > mid:
                    dict[s[left]] -= 1
                    left += 1

                right += 1

                max_count = max(max_count, min(mid, max(dict.values())))
            if mid - max_count <= k:
                return True

        s = list(s)
        left = 1
        right = len(s) - 1
        max_length = 0
        while left <= right:
            mid = (left + right) // 2
            valid = calculate_change(s, k, mid)

            if valid:
                left = mid + 1
            else:
                 right = mid - 1
        return left