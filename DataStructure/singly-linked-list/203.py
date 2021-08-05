from singly_linked_list_utils import *

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return head

        start_node = head

        # delete list
        while start_node:
            if start_node.val == val:
                start_node = start_node.next
            else:
                break

        if start_node == None:
            return start_node


        delet_node = None



# linked_list = [1,2,6,3,4,5,6]
linked_list = [1,2,2,1]
root_node = create_singly_linked_list(linked_list)
val = 2

solution = Solution()
opt = solution.removeElements(root_node, val)
print(opt)