def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if(not head): return head

    new_head = head
    while(new_head.next):
        new_head = new_head.next
    tail = new_head

    while(new_head != head):
        move = head
        head = head.next
        move.next = tail.next
        tail.next = move

    return new_head
