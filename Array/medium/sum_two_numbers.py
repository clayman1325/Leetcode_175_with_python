class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while(left < right):
            if((numbers[right] + numbers[left]) == target): return [left + 1, right + 1]

            if(abs(target - (numbers[right] + numbers[left] + 1)) < abs(target - (numbers[left] + numbers[right] - 1))):
                left += 1
            else:
                right -= 1