class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self._head = Node(0)
        self._count = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self._count:
            return -1

        node = self._head.next
        while index:
            index = index - 1
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self._count, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        if index > self._count:
            return
        
        add_node = Node(val)
        pre_node, cur_node = None, self._head
        for _ in range(index + 1):
            pre_node, cur_node = cur_node, cur_node.next
        pre_node.next, add_node.next = add_node, cur_node
        self._count += 1

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self._count:
            # 计数-1
            self._count -= 1
            prev_node, current_node = None, self._head
            for _ in range(index + 1):
                prev_node, current_node = current_node, current_node.next
            else: # python的for-else语法：正常循环退出执行，break不执行
                prev_node.next, current_node.next = current_node.next, None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


class ListNode:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self._head, self._tail = ListNode(0), ListNode(0)
        self._head.next, self._tail.pre = self._tail, self._head
        self._count = 0

    def _get_node(self, index):
        if index >= self._count//2:
            node = self._tail
            for _ in range(self._count - index):
                node = node.pre
        else:
            node = self._head
            for _ in range(index + 1):
                node = node.next
        return node

    def get(self, index: int) -> int:
        if 0 <= index < self._count:
            node = self._get_node(index)
            return node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self._update_node(self._head, self._head.next, val)

    def addAtTail(self, val: int) -> None:
        self._update_node(self._tail.pre, self._tail, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        if index > self._count:
            return
        
        node = self._get_node(index)
        self._update_node(node.pre, node, val)
        

    def _update_node(self, pre, next, val):
        self._count += 1
        node = ListNode(val)
        pre.next, next.pre = node, node
        node.pre, node.next = pre, next


    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self._count:
            node = self._get_node(index)
            # 计数-1
            self._count -= 1
            node.pre.next, node.next.pre = node.next, node.pre
