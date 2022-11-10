# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self._head = ListNode(next=head)
        pre = self._head
        cur = head
        
        while cur and cur.next:
            tmp = cur.next.next
            pre.next = cur.next
            cur.next.next = cur
            cur.next = tmp
            pre = cur
            cur = tmp
        
        return self._head.next
    
