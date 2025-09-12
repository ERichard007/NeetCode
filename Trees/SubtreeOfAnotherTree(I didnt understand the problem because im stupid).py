from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:   
    def findMatchingRootLeft(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not subRoot:
            return None
        elif subRoot.val == root.val:
            return root
        
        leftSearch = self.findMatchingRootLeft(root.left, subRoot)

        return leftSearch


    def findMatchingRootRight(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not subRoot:
            return None
        elif subRoot.val == root.val:
            return root
        
        rightSearch = self.findMatchingRootRight(root.right, subRoot)

        return rightSearch


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        leftMatchingRoot = self.findMatchingRootLeft(root, subRoot)
        rightMatchingRoot = self.findMatchingRootRight(root, subRoot) if leftMatchingRoot == None else None

        print("ROOT: " + str(root.val))
        print(leftMatchingRoot.val if leftMatchingRoot != None else None)
        print(rightMatchingRoot.val if rightMatchingRoot != None else None)
        print("**************")

        if leftMatchingRoot == rightMatchingRoot:
            return True

        doesMatchLeftSubTree = self.isSubtree(leftMatchingRoot if leftMatchingRoot != None else rightMatchingRoot, subRoot.left)
        doesMatchRightSubTree = self.isSubtree(leftMatchingRoot if leftMatchingRoot != None else rightMatchingRoot, subRoot.right)

        return (doesMatchLeftSubTree and doesMatchRightSubTree)
    
mySolution = Solution()

Tree = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3))
SubTree = TreeNode(2,TreeNode(4),TreeNode(5)) #true

Tree2 = TreeNode(1,TreeNode(2,TreeNode(4,TreeNode(6)),TreeNode(5)),TreeNode(3))
SubTree2 = TreeNode(2,TreeNode(4),TreeNode(5)) #false

print(mySolution.isSubtree(Tree, SubTree))
print(mySolution.isSubtree(Tree2, SubTree2))