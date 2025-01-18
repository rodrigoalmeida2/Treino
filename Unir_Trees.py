# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 and not root2:
            return None

        new_node = TreeNode()

        if root1:
            new_node.val = root1.val

        if root2:
            new_node.val += root2.val

        new_node.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        new_node.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

        return new_node

# Example usage:
# Construct Tree 1
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

# Construct Tree 2
root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(7)

# Merge the trees
merged_tree = Solution().mergeTrees(root1, root2)

# Helper function to print the tree (for visualization)
def print_tree(root):
    if root:
        print(root.val, end=" ")
        print_tree(root.left)
        print_tree(root.right)

# Print the merged tree
print_tree(merged_tree)