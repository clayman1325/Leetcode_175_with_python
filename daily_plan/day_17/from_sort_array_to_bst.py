class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def divide(nums):
            if len(nums) == 1:
                return TreeNode(nums[0])

            mid = len(nums) // 2

            root = TreeNode(nums[mid])

            if nums[:mid]: root.left  = divide(nums[:mid])
            if nums[mid+1:]: root.right = divide(nums[mid+1:])

            return root

        return divide(nums)