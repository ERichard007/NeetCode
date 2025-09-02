from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        return max(1 + (self.maxDepth(root.left)),1 + (self.maxDepth(root.right)))
    
mySolution = Solution()

tree = TreeNode(1,TreeNode(2),TreeNode(3,TreeNode(4)))

print(mySolution.maxDepth(tree))