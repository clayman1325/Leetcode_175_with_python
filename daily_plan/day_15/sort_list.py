# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(list_a, list_b):
            if list_a.val < list_b.val:
                merged = list_a
                second = list_b
            else:
                merged = list_b
                second = list_a
            result = merged
            prev = merged

            while(merged and second):
                prev = merged
                if merged.next and merged.next.val <= second.val:
                    merged = merged.next
                else:
                    merging = second
                    second = second.next
                    merging.next = merged.next
                    merged.next = merging
                    merged = merged.next

            if not merged:
                prev.next = second

            return result

        def merge_sort(head):
            if not head.next:
                return head

            list_a = head
            slow = head
            fast = head
            while(fast.next and fast.next.next):
                slow = slow.next
                fast = fast.next.next
            list_b = slow.next
            slow.next = None

            left  = merge_sort(list_a)
            right = merge_sort(list_b)

            return merge(left, right)

        if not head or not head.next: return head
        return merge_sort(head)