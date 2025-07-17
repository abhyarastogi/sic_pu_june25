class TreeNode:
    def __init__(self, x):
        self.x = x
        self.L = None
        self.R = None

def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.x:
        root.L = insert(root.L, val)
    else:
        root.R = insert(root.R, val)
    return root

def height(node):
    if node is None:
        return -1
    return 1 + max(height(node.L), height(node.R))

# Sample Input
values = [4, 2, 1, 3, 6, 7, 5]
root = None
for v in values:
    root = insert(root, v)

print(height(root))  # Output should be 2
