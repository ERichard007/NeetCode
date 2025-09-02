from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        width = self.diameterOfBinaryTree(root.left) + self.diameterOfBinaryTree(root.right) + 1

        return width

mySolution = Solution()

tree = TreeNode(1,TreeNode(2),TreeNode(3))

print(mySolution.diameterOfBinaryTree(tree))