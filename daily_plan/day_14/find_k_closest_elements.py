class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        mid = 0
        distance = 100000
        for idx, num in enumerate(arr):
            val = abs(num - x)
            if  val < distance:
                distance = val
                mid = idx
        left  = mid - 1
        right = mid + 1
        output = [arr[mid]]

        while right - left - 1 < k:
            if left == -1:
                right += 1
                continue
            if right == len(arr) or abs (arr[left] - x) <= abs(arr[right] -x):
                left -= 1
            else:
                right += 1

        return arr[left +1:right]