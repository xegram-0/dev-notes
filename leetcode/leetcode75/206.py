# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fakeNode = ListNode()
        prev = None
        current = head
        while current is not None:
            nextNode = current.next
            current.next = fakeNode.next
            fakeNode.next = current
            current = nextNode
        return fakeNode.next
