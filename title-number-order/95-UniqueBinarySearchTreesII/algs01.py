# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int):

        for nn in range(n):
            left_nums = range(nn)
            right_nums = range(nn, n)
            root_node = TreeNode(nn, )


    def inorder_visit(self, visit_list, bt_node):
        if bt_node != None:
            self.inorder_visit(visit_list, bt_node.left)
            visit_list.append(bt_node.val)
            self.inorder_visit(visit_list, bt_node.right)