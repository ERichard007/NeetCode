from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:   

    def DFS(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        elif root.val == target:
            return root
        
        leftSearch = self.DFS(root.left, target)
        rightSearch = self.DFS(root.right, target)

        return leftSearch or rightSearch
    
    def IsSameTree(self, root: TreeNode, subroot: TreeNode) -> bool:
        if not root and not subroot:
            return True
        elif (not root or not subroot) or (root.val != subroot.val):
            return False

        leftward = self.IsSameTree(root.left, subroot.left)
        rightward = self.IsSameTree(root.right, subroot.right)

        return (leftward and rightward)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root.val != subRoot.val:
            leftSearch = self.DFS(root.left, subRoot.val)
            rightSearch = self.DFS(root.right, subRoot.val)

            root = leftSearch or rightSearch

            if not root:
                return False
            
        testRoot = self.IsSameTree(root, subRoot)
        leftRoot = root.left
        rightRoot = root.right

        while not testRoot and (leftRoot or rightRoot):
            
            left = self.IsSameTree(leftRoot, subRoot)
            right = self.IsSameTree(rightRoot, subRoot)

            leftRoot = leftRoot.left if leftRoot != None else None
            rightRoot = rightRoot.right if rightRoot != None else None

            testRoot = left or right

        return testRoot
    
mySolution = Solution()

Tree = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3))
SubTree = TreeNode(2,TreeNode(4),TreeNode(5)) 

Tree2 = TreeNode(1,TreeNode(2,TreeNode(4,TreeNode(6)),TreeNode(5)),TreeNode(3))
SubTree2 = TreeNode(2,TreeNode(4),TreeNode(5)) 

Tree3 = TreeNode(3,TreeNode(4,TreeNode(1),TreeNode(2)),TreeNode(5))
SubTree3 = TreeNode(4,TreeNode(1,TreeNode(1)),TreeNode(2)) 

Tree4 = TreeNode(1,TreeNode(1))
SubTree4 = TreeNode(1)

print(mySolution.isSubtree(Tree, SubTree)) #true
print(mySolution.isSubtree(Tree2, SubTree2)) #false
print(mySolution.isSubtree(Tree3, SubTree3)) #false
print(mySolution.isSubtree(Tree4, SubTree4)) #true