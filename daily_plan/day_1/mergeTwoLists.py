def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if(list1 is None and list2 is None): return list1
    if(list2 is None): return list1
    if(list1 is None): return list2

    if(list1.val <= list2.val):
        base_list = list1
        other_list = list2
    else:
        base_list = list2
        other_list = list1
    result = base_list

    while(base_list is not None or other_list is not None):
        base_next = base_list.next
        if(base_list.next is None):
            base_list.next = other_list
            return result
        if(other_list is None):
            return result
        if(base_next.val <= other_list.val):
            base_list = base_list.next
        else:
            aux = other_list
            other_list = other_list.next
            aux.next = None
            base_list.next = aux
            base_list.next.next = base_next
            base_list = base_list.next

    return result