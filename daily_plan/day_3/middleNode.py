def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head
    while(fast and fast.next and fast.next.next):
        slow = slow.next
        fast = fast.next.next

    return slow.next if fast.next else slow