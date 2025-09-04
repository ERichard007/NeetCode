from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def leftHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return  0
        
        left = 1 + (self.leftHeight(root.left))
        right = 1 + (self.rightHeight(root.right))

        return max(left,right)

    def rightHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = 1 + (self.rightHeight(root.left))
        right = 1 + (self.rightHeight(root.right))

        return max(left,right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:   
        if not root:
            return True

        leftHeight = 1 + self.leftHeight(root.left)
        rightHeight = 1 + self.rightHeight(root.right)
        print("node: " + str(root.val) + " left: " + str(leftHeight) + " right: " + str(rightHeight))

        leftHeight = leftHeight + 1 if leftHeight < rightHeight else leftHeight
        rightHeight = rightHeight + 1 if rightHeight < leftHeight else rightHeight

        isBalanced = leftHeight==rightHeight and self.isBalanced(root.left) and self.isBalanced(root.right)

        return(isBalanced)
    
tree = TreeNode(1,TreeNode(2),TreeNode(3,TreeNode(4))) #true
tree2 = TreeNode(1,TreeNode(2),TreeNode(3,TreeNode(4,TreeNode(5)))) #false
tree3 = TreeNode(None) #true
myTree = TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4,None,TreeNode(5,None,TreeNode(6)))),TreeNode(7,None,TreeNode(8,None,TreeNode(9,None,TreeNode(10)))))


mySolution = Solution()
print(mySolution.isBalanced(myTree))
