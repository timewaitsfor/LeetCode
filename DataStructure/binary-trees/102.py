from .binary_tree_utils import *


class Solution:
    def levelOrder(self, root):

        if root == None:
            return []

        memo = []
        node_level = 0
        node_level_dict = {}
        memo.append(root)
        node_level_dict[root] = node_level

        while True:

            if len(memo) == 0:
                break

            node = memo.pop(0)
            this_node_level = node_level_dict[node]

            if node.left == None and node.right == None:
                continue

            if node.left != None:
                memo.append(node.left)
                node_level_dict[node.left] = this_node_level + 1
            if node.right != None:
                memo.append(node.right)
                node_level_dict[node.right] = this_node_level + 1

        opt = {}
        for k, v in node_level_dict.items():
            if v not in opt:
                opt[v] = []
                opt[v].append(k.val)
            else:
                opt[v].append(k.val)

        return list(opt.values())


# node_list = [3,9,20,None,None,15,7]
node_list = [1, 2]
node = create_binary_tree(node_list)

solution = Solution()
print(solution.levelOrder(node))

