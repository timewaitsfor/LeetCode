# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildSubTree(self, preorder, inorder_start, inorder_end):
        if len(preorder) == 0:
            return None

        treeNode = TreeNode()
        rootNode = preorder[0]
        treeNode.val = rootNode

        if len(preorder) == 1:
            return treeNode

        thisNode_idx = self.inorder_dict[rootNode]
        leftLen = thisNode_idx - inorder_start
        rightLen = inorder_end - thisNode_idx

        left_preorder = preorder[1:leftLen + 1]
        right_preorder = preorder[leftLen + 1:leftLen + 1 + rightLen]

        left_inorder_start = inorder_start
        left_inorder_end = inorder_start + leftLen

        right_inorder_start = inorder_end - rightLen + 1
        right_inorder_end = inorder_end

        # 左子树
        treeNode.left = self.buildSubTree(left_preorder, left_inorder_start, left_inorder_end)
        # 右子树
        treeNode.right = self.buildSubTree(right_preorder, right_inorder_start, right_inorder_end)

        return treeNode

    def buildTree(self, preorder, inorder):
        # preorder_dict = {pv:pi for pi, pv in enumerate(preorder)}
        self.inorder_dict = {iv: ii for ii, iv in enumerate(inorder)}
        return self.buildSubTree(preorder, 0, len(inorder) - 1)



solution = Solution()
opt = solution.buildTree([3,9,20,15,7],[9,3,15,20,7])
print(opt)
