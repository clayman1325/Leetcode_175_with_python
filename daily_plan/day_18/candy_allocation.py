class Solution:
    def candy(self, ratings: List[int]) -> int:
        left = [1] * len(ratings)
        right = [1] * len(ratings)
        merge = [1] * len(ratings)
        count = 0
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                left[i] = left[i-1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1] + 1
        for i in range(len(ratings)):
            merge[i] = max(left[i], right[i])
            count += merge[i]
        return count