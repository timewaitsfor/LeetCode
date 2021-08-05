
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_binary_tree(tree_list):

    root_node = TreeNode()
    root_node.val = tree_list[0]
    tree_queue = [root_node]
    node_idx = 1

    while True:
        if node_idx == len(tree_list):
            break

        this_node = tree_queue.pop(0)

        if tree_list[node_idx] != None:
            this_node.left = TreeNode()
            this_node.left.val = tree_list[node_idx]
            tree_queue.append(this_node.left)
        node_idx += 1

        if node_idx == len(tree_list):
            break

        if tree_list[node_idx] != None:
            this_node.right = TreeNode()
            this_node.right.val = tree_list[node_idx]
            tree_queue.append(this_node.right)
        node_idx += 1

    return root_node




if __name__ == '__main__':
    tree_list = [1, 2, 2, 3, 4, 4, 3]
    root_node = create_binary_tree(tree_list)
    pass

