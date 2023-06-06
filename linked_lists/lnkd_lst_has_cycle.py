class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while(head):
            if(head.val == "#"):
                return True
            head.val = "#"
            head = head.next

        return Falsemb\