from typing import Optional



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def heighOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max((self.heighOfBinaryTree(root.left), self.heighOfBinaryTree(root.right)))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftHeight = self.heighOfBinaryTree(root.left)
        rightHeight = self.heighOfBinaryTree(root.right)
        currentNodeDiameter = leftHeight + rightHeight 

        print("Current root: " + str(root.val) + " diameter: " + str(currentNodeDiameter))

        subTree = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), currentNodeDiameter)

        print("Current root: " + str(root.val) + " subTreeVal: " + str(subTree) + " currentNodeDiameter: " + str(currentNodeDiameter))

        return max(currentNodeDiameter, subTree)

mySolution = Solution()

tree = (TreeNode(1,None,TreeNode(3,TreeNode(4,TreeNode(6),TreeNode(7)),TreeNode(5,TreeNode(8),TreeNode(9)))))

print(mySolution.diameterOfBinaryTree(tree))

