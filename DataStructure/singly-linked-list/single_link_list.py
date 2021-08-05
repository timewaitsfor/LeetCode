# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        pass

solu = Solution()

list1 = [1,2,4]
list2 = [1,3,4]

def constract_single_link_list(simple_list):
    dummy = ListNode(simple_list[0])
    cur = dummy
    for i in range(1, len(simple_list)):
        this_val = simple_list[i]
        this_node = ListNode(this_val)
        if i < len(simple_list):
            cur.next = this_node
        else:
            cur.next = None
        cur = cur.next
    return dummy

l1 = constract_single_link_list(list1)
l2 = constract_single_link_list(list2)

temp = l1
for j in range(3):
    print(temp.val)
    temp = temp.next


res = solu.mergeTwoLists(l1, l2)
print(res)