import numpy;
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder_print(node):
    if node:
        print(node.data, end=' ')
        preorder_print(node.left)
        preorder_print(node.right)

# Example Usage
if __name__ == "__main__":
    # Create the tree
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Perform preorder traversal and print nodes
    preorder_print(root)
