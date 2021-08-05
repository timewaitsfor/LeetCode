from binary_tree_utils import *

class Solution:
    def isSymmetric(self, root):
        pair_node_queue = []

        if root.left == None and root.right == None:
            return True
        elif root.left == None and root.right != None:
            return False
        elif root.left != None and root.right == None:
            return False
        else:
            pair_node_queue.append(root.left)
            pair_node_queue.append(root.right)

        while True:
            if len(pair_node_queue) < 2:
                break
            left_node = pair_node_queue.pop(0)
            right_node = pair_node_queue.pop(0)

            if left_node.val != right_node.val:
                return False

            if left_node.left == None and right_node.right == None:
                pass
            elif left_node.left == None and right_node.right != None:
                return False
            elif left_node.left != None and right_node.right == None:
                return False
            else:
                pair_node_queue.append(left_node.left)
                pair_node_queue.append(right_node.right)

            if left_node.right == None and right_node.left == None:
                pass
            elif left_node.right == None and right_node.left != None:
                return False
            elif left_node.right != None and right_node.left == None:
                return False
            else:
                pair_node_queue.append(left_node.right)
                pair_node_queue.append(right_node.left)

        return True



# node_list = [1,2,2,3,4,4,3]
node_list = [1,2,2,None,3,None,3]
root_node = create_binary_tree(node_list)

solution = Solution()
opt = solution.isSymmetric(root_node)
print(opt)