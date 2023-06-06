class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        total = ListNode(val=0)
        result = total
        while(l2 and l1):
            first_val = l1.val if l1.val else 0
            second_val = l2.val if l2.val else 0

            cur_sum =  int(first_val + second_val + carry)
            value = int(cur_sum % 10)
            carry = int(cur_sum / 10)
            total.val = value
            if(l2.next or l1.next):
                total.next = ListNode()
                total = total.next

            l1 = l1.next
            l2 = l2.next

        if(l2):
            while(l2):
                cur_sum =  int(l2.val + carry)
                value = int(cur_sum % 10)
                carry = int(cur_sum / 10)

                total.val = value

                if(l2.next):
                    total.next = ListNode()
                    total = total.next

                l2 = l2.next
        if(l1):
            while(l1):
                cur_sum =  int(l1.val + carry)
                value = int(cur_sum % 10)
                carry = int(cur_sum / 10)

                total.val = value

                if(l1.next):
                    total.next = ListNode()
                    total = total.next

                l1 = l1.next

        if(carry > 0):
            total.next = ListNode()
            total = total.next
            total.val = carry

        return result