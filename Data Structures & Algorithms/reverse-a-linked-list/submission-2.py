# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

# the triple pointer is the best approach, pre, cur, post the curr.next becomes pre, pre becomes curr, curr becomes post, post = post.next, at the end you return pre as it becomes the last which is the first.