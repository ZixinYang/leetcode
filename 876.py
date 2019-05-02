'''
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.
'''

# Tags: Two Pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head: return None
        slow = head
        fast = head
        f_step = 0
        while fast:
            if fast.next:
                slow = slow.next
                fast = fast.next.next
                f_step+=2
            else:
                break
        if f_step%2==1:
            return slow.next
        else:
            return slow