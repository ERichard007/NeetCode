from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:   

    def leftDFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        elif root.left == None:
            return root
        
        return self.leftDFS(root.left)

    def rightDFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        elif root.right == None:
            return root
        
        return self.rightDFS(root.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if root.val != subRoot.val:
            searchLeftTree = self.isSubtree(root.left, subRoot)
            searchRightTree = self.isSubtree(root.right, subRoot)

            return searchLeftTree or searchRightTree

        leftSubrootDFS = self.leftDFS(subRoot)
        rightSubrootDFS = self.rightDFS(subRoot)
        leftTreeDFS = self.leftDFS(root.left)
        rightTreeDFS = self.rightDFS(root.right)

        print("ROOT: " + str(root.val))
        print(leftSubrootDFS.val)
        print(rightSubrootDFS.val)
        print(leftTreeDFS.val)
        print(rightTreeDFS.val)

        print("******************")

        return (leftSubrootDFS.val == leftTreeDFS.val and rightSubrootDFS.val == rightTreeDFS.val)
    
mySolution = Solution()

Tree = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3))
SubTree = TreeNode(2,TreeNode(4),TreeNode(5)) 

Tree2 = TreeNode(1,TreeNode(2,TreeNode(4,TreeNode(6)),TreeNode(5)),TreeNode(3))
SubTree2 = TreeNode(2,TreeNode(4),TreeNode(5)) 

Tree3 = TreeNode(3,TreeNode(4,TreeNode(1),TreeNode(2)),TreeNode(5))
SubTree3 = TreeNode(4,TreeNode(1),TreeNode(2)) 

print(mySolution.isSubtree(Tree, SubTree)) #true
print(mySolution.isSubtree(Tree2, SubTree2)) #false
print(mySolution.isSubtree(Tree3, SubTree3)) #false