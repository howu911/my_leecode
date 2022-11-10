# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        pre = None
        cur = head
        next = head.next

        while next:
            cur.next = pre
            pre = cur
            cur = next
            next = cur.next
        
        cur.next = pre
        
        return cur
    
#双指针
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head   
        pre = None
        while(cur!=None):
            temp = cur.next # 保存一下 cur的下一个节点，因为接下来要改变cur->next
            cur.next = pre #反转
            #更新pre、cur指针
            pre = cur
            cur = temp
        return pre


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        def reverse(pre,cur):
            if not cur:
                return pre
                
            tmp = cur.next
            cur.next = pre

            return reverse(cur,tmp)
        
        return reverse(None,head)