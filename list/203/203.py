# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# myself
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head:
            if head.val == val:
                head = head.next
            else:
                break
        
        if not head or not head.next:
            return head
        
        pre = head
        cur = head.next

        while cur:
            if cur.val == val:
                pre.next = cur.next
                cur = cur.next
            else:
                pre = cur
                cur = cur.next

        return head
    

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 删除头结点
        while head and head.val == val:
            head = head.next
        
        # 删除非头结点
        cur = head
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


# 使用虚拟头指针的方法
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        virtual_head = ListNode()
        virtual_head.next = head
        
        cur = virtual_head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return virtual_head.next

