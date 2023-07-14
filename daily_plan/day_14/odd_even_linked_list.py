class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        odd = head
        even = head.next

        node_a = head
        while node_a and  node_a.next:
            next_node = node_a.next
            node_a.next = node_a.next.next
            node_a.next = next_node

        odd_tail = odd
        while odd_tail.next and odd_tail.next.next:
            odd_tail = odd_tail.next.next
        if odd_tail.next: odd_tail = odd_tail.next
        odd_tail.next = even
        return odd