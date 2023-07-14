class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap(pre,node_a, node_b):
            if pre: pre.next = node_b
            node_a.next = node_b.next
            node_b.next = node_a

        if not head: return head
        if not head.next: return head
        result = head.next
        node_a = head
        node_b = head.next
        pre = None
        while(node_a.next):
            swap(pre, node_a, node_b)
            pre = node_a
            node_a = node_a.next
            if not node_a: return result
            node_b = node_a.next
            if not node_b: return result

        return result