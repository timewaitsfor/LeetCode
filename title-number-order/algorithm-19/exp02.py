
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        p = dummy
        q = dummy

        for i in range(n):
            p = p.next

        if p.next == None:
            q.next = q.next.next
            return dummy.next

        while True:
            p = p.next
            q = q.next
            if p.next == None:
                break
        q.next = q.next.next

        return dummy.next


head = [1]
n = 1

list_node = ListNode(1, None)

solu = Solution()
res = solu.removeNthFromEnd(list_node, n)
print(res)