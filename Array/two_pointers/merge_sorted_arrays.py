class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m-1
        j = n-1
        index = m+n-1

        while i>= 0 and j >= 0:
            if(nums1[i] > nums2[j]):
                nums1[index] = nums1[i]
                i -= 1
                index -= 1
            elif nums2[j] > nums1[i]:
                nums1[index] = nums2[j]
                j -= 1
                index -= 1
            else:
                nums1[index] = nums1[i]
                nums1[index-1] = nums2[j]
                i -= 1
                j -= 1
                index -= 2

        while j >= 0:
            nums1[index] = nums2[j]
            j -= 1
            index -= 1
