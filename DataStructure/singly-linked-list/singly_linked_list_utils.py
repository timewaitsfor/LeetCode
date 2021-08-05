# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_singly_linked_list(linked_list):
    root_node = ListNode()
    root_node.val = linked_list[0]
    last_node = root_node
    for linked_node in linked_list[1:]:
        this_node = ListNode()
        this_node.val = linked_node

        last_node.next = this_node
        last_node = this_node

    return root_node

if __name__ == '__main__':
    linked_list = [1,2,6,3,4,5,6]
    root_node = create_singly_linked_list(linked_list)
    pass