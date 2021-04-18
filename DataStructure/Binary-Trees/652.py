# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root):

        if root.left == None and root.right == None:
            this_tree_str = str(root.val)
        else:
            if root.left != None:
                left_tree_str = self.traverse(root.left)
            else:
                left_tree_str = '#'
            if root.right != None:
                right_tree_str = self.traverse(root.right)
            else:
                right_tree_str = '#'
            this_tree_str = left_tree_str + "_" + str(root.val) + "_" + right_tree_str

        if this_tree_str in self.duplicate_subtrees:
            self.duplicate_subtrees[this_tree_str] += 1
            if self.duplicate_subtrees[this_tree_str] == 2:
                self.duplicate_roots.append(root)
        else:
            self.duplicate_subtrees[this_tree_str] = 1

        return this_tree_str

    def findDuplicateSubtrees(self, root):

        if root.left == None and root.right == None:
            return None

        self.duplicate_subtrees = {}
        self.duplicate_roots = []
        self.traverse(root.left)
        self.traverse(root.right)

        return self.duplicate_roots


solution = Solution()
# opt = solution.findDuplicateSubtrees([0,None,0,0,None,0,0,null,0,null,0,0])
# print(opt)