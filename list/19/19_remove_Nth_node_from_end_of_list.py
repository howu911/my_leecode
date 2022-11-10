# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self._head = ListNode(next=head)
        pre, last = self._head, self._head
        
        while n:
            pre = pre.next
            n -= 1
        
        while pre.next:
            pre = pre.next
            last = last.next
        last.next = last.next.next
        
        return self._head.next
        