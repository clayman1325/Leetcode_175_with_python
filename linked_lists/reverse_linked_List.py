def reverseList4(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap(prev_head, head, prev_tail):
            tail      = prev_tail.next
            head_next = head.next
            tail_next = tail.next
            head.next = None
            tail.next = None

            aux = head

            head = tail
            if(prev_head): prev_head.next = head
            head.next = head_next

            tail = aux
            prev_tail.next = tail
            tail.next = tail_next

            return head

        if(not head or not head.next): return head
        length  = 0
        tail    = head
        pointer = 0

        while(tail.next):
            tail = tail.next
            length += 1

        result = tail
        prev_head = None

        while(pointer < length // 2):
            prev_tail = head
            count = 0

            while(count < length - 1):
                prev_tail = prev_tail.next
                count += 1
            prev_head = swap(prev_head, head, prev_tail)
            head = prev_head.next
            length -= 2

        if(length == 1):
            if(prev_head):
                prev_head.next = head.next
            aux = head
            next_head = head.next.next
            head = head.next
            head.next = aux
            head.next.next = next_head




        return result



    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head or not head.next): return head
        new_head = head.next
        new_head_next = new_head.next
        rh = head
        rh.next = None
        head = new_head
        head.next = new_head_next

        while(head.next):
            new_head = head.next
            new_head_next = head.next.next
            head.next = rh
            rh = head
            head = new_head
            head.next = new_head_next
        head.next = rh
        return head


    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head or not head.next): return head
        tail = head
        while(tail.next != None):
            tail = tail.next
        while(head != tail):
            move = head
            head = head.next
            move.next = tail.next
            tail.next = move

        return tail