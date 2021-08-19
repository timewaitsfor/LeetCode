from singly_linked_list_utils import *


class Solution:
    def get_head_tail_node(self, head):
        if head.next != None:
            next_node = head.next
        else:
            return head, head
        next_head, next_tail = self.get_head_tail_node(next_node)
        next_tail.next = head
        head.next = None

        return next_head, head

    def reverseList(self, head):
        if head == None:
            return head
        this_node = head
        next_node = head.next

        if next_node == None:
            return head

        next_head, next_tail = self.get_head_tail_node(next_node)
        next_tail.next = this_node
        this_node.next = None

        return next_head


linked_list = [1,2,3,4,5]
root_node = create_singly_linked_list(linked_list)

solution = Solution()
opt = solution.reverseList(root_node)
print(opt)