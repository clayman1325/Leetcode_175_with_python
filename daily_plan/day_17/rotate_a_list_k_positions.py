class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        if k < 1: return  head

        first = head
        tail = head
        length = 1
        while tail and tail.next:
            tail = tail.next
            length += 1

        tail.next = first
        head = first
        next_tail = head

        count = 0
        while count < (length - k % length - 1):
            next_tail = next_tail.next
            count += 1
        head = next_tail.next
        next_tail.next = None

        return head