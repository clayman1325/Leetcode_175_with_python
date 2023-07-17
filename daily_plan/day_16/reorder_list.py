class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def merge_lists(left , right):
            result = left
            while(right):
                aux = left.next
                left.next = right
                left = aux
                aux = right.next
                right.next = left
                right = aux

            return result

        def reverse_list(head):
            tail = head
            while(tail.next):
                tail = tail.next

            while head != tail:
                swap = head
                head = head.next
                swap.next = tail.next
                tail.next = swap
            return tail
        if not head.next: return head

        left = head
        slow = head
        fast = head
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None

        right = reverse_list(right)

        head = merge_lists(left , right)