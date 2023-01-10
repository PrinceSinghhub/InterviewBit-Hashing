# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        curr = head
        while curr:
            node = RandomListNode(curr.label)
            temp = curr.next
            curr.next = node
            node.next = temp
            curr = curr.next.next
        curr = head
        while curr:
            temp = curr.next.next
            curr.next.next = temp.next if temp else None
            curr.next.random = curr.random.next if curr.random else None
            curr = temp

        return head.next
