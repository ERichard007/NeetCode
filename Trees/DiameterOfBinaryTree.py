from typing import Optional



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    MAX_D = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        leftHeight = self.diameterOfBinaryTree(root.left) + 1
        rightHeight = self.diameterOfBinaryTree(root.right) + 1

        self.MAX_D = max(leftHeight+rightHeight, self.MAX_D)

        print("root value: " + str(root.val) + " left height: " + str(leftHeight) + " right height: " + str(rightHeight) + " max depth: " + str(self.MAX_D))

        return max(leftHeight,rightHeight)
        

mySolution = Solution()

tree = TreeNode(1,None,TreeNode(2,TreeNode(3,TreeNode(5)), TreeNode(4)))

mySolution.diameterOfBinaryTree(tree)

print(mySolution.MAX_D)