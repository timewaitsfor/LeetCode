# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildSubTree(self, postorder, inorder_start, inorder_end):
        if len(postorder) == 0:
            return None
        treeNode = TreeNode()
        rootNode = postorder[-1]
        treeNode.val = rootNode

        if len(postorder) == 1:
            return treeNode

        thisNode_idx = self.inorder_dict[rootNode]
        leftLen = thisNode_idx - inorder_start
        rightLen = inorder_end - thisNode_idx

        right_postorder = postorder[-1 - rightLen:-1]
        left_postorder = postorder[-1 - rightLen - leftLen:-1 - rightLen]

        left_inorder_start = inorder_start
        left_inorder_end = inorder_start + leftLen -1

        right_inorder_start = inorder_end - rightLen
        right_inorder_end = inorder_end

        if leftLen > 0:
            treeNode.left = self.buildSubTree(left_postorder, left_inorder_start, left_inorder_end)
        else:
            treeNode.left = None

        if rightLen > 0:
            treeNode.right = self.buildSubTree(right_postorder, right_inorder_start, right_inorder_end)
        else:
            treeNode.right = None

        return treeNode

    def buildTree(self, inorder, postorder):
        self.inorder_dict = {iv: ii for ii, iv in enumerate(inorder)}
        # preorder = postorder[::-1]
        return self.buildSubTree(postorder, 0, len(inorder) - 1)



solution = Solution()
opt = solution.buildTree([3,2,1],[3,2,1])
print(opt)
