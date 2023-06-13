class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def buildDict(array):
            freq = {}
            for x in array:
                if freq.get(x):
                    freq[x] += 1
                else:
                    freq[x] = 1
            return freq

        frequencies = buildDict(nums)

        target = len(nums) / 2

        for x in frequencies:
            if(frequencies.get(x) > target): return x