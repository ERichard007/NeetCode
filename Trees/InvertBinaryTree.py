from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if (root == None):
            return None
        elif (root.left == None and root.right == None):
            return root
        
        leftRoot = self.invertTree(root.left)
        rightRoot = self.invertTree(root.right)       

       
        temp = leftRoot
        root.left = rightRoot
        root.right = temp
        
        return root

    
root = TreeNode(1,TreeNode(2, TreeNode(4), TreeNode(5)),TreeNode(3, TreeNode(6), TreeNode(7)))

mySolution = Solution()
mySolution.invertTree(root)