# class TreeNode:
def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:

    def preorder(self, root):
        if root == None:
            return ['#']
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)

    def postorder(self, root):
        if root == None:
            return ['#']
        return self.preorder(root.left) + self.preorder(root.right) + [root.val]

    def isSymmetric(self, root):

        if root == None:
            return False

        left_list = self.preorder(root.left)
        right_list = self.postorder(root.right)

        if left_list == right_list[::-1]:
            return True
        else:
            return False

solution = Solution()
opt = solution.isSymmetric([3,2,1],[3,2,1])
print(opt)