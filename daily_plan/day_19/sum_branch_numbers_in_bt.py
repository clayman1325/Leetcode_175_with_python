class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sum_num(num, exp):
            if not num:
                return 0
            cur_num = num.pop() * 10 ** exp
            return cur_num + sum_num(num, exp + 1)
        def dfs(root, cur_sum, total):
            if root and not root.left and not root.right:
                cur_sum = cur_sum + [root.val]
                total.append(cur_sum)
            if not root:
                return

            dfs(root.left, cur_sum + [root.val], total)
            dfs(root.right, cur_sum + [root.val], total)

        total = []
        cur_sum = []
        dfs(root, [],total)
        cur_sum = 0
        for t in total:
            cur_sum += sum_num(t, 0)
        return cur_sum