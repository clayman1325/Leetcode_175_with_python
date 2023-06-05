class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if(len(nums) == 0): return ""

        ranges = []
        cur_range = []

        for num in nums:
            if(len(cur_range) == 0):
                cur_range.append(num)
            elif(num == cur_range[len(cur_range) - 1] +1):
                if(len(cur_range) == 1):
                    cur_range.append(num)
                else:
                    cur_range[1] = num
            else:
                ranges.append(cur_range)
                cur_range = [num]

        ranges.append(cur_range)

        result = []
        for range in ranges:
            if (len(range) == 2):
                value = f'{range[0]}->{range[1]}'
            else:
                value = f'{range[0]}'

            result.append(value)

        return result
