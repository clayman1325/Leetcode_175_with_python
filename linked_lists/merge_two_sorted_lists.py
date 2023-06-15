# Question 21. Merge Two Sorted Lists
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.


# Input: list1 = [1, 1,  2, 3,4, 4], list2 = [1,3,4]
#                                           H                     h
# result_head = 1

# Output: [1,1,2,3,4,4]

# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]

# 	Test:
# List 1 = 3,4, list2 = [4]
# Current_head = 1, 1 , 2, 3,4,4
#                          L1
# Aux 4
# List2 = null
# Aux.next = 4
# List1.next = 4
# list1= 4


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(list1 is None and list2 is None): return list1
        if(list2 is None ): return list1
        if(list1 is None ): return list2

        [list1, list2] = [list1, list2] if list1.val <= list2.val else [list2, list1]
        result_head = list1

        while(list1 is not None or list2 is not None):
            if(list2 is None):
                return result_head
            if(list1 is None):
                list1.next = list2
                return result_head
            if(list1.next and list1.next.val < list2.val):
                list1 = list1.next
            else:
                aux = list2
                list2 = list2.next
                aux.next = list1.next
                list1.next = aux
                list1 = list1.next

        return result_head


# Pseudo code:
# Find the min value from two linkedlist
# Store that head and in the end return this head
# Start adding elements to that linked list comparing the head of the other with the current node.
# Return first min head
