# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        newHead = None

        while head != None:
            preHead = ListNode()
            preHead = ListNode(head.val,newHead)
            newHead = preHead
            head = head.next
        
        return preHead

