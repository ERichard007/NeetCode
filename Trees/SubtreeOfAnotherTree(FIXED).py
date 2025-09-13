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
    
    def FindDepth(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        elif not root.left and not root.right:
            return root
        
        leftSearch = self.FindDepth(root.left)
        rightSearch = self.FindDepth(root.right)

        return leftSearch or rightSearch

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root.val != subRoot.val:
            leftSearch = self.DFS(root.left, subRoot.val)
            rightSearch = self.DFS(root.right, subRoot.val)

            root = leftSearch or rightSearch

            if not root:
                return False

        subRootLeftDFS = self.FindDepth(subRoot.left)
        subRootRightDFS = self.FindDepth(subRoot.right)
        treeLeftDFS = self.FindDepth(root.left)
        TreeRightDFS = self.FindDepth(root.right)

        print(subRootLeftDFS.val)
        print(treeLeftDFS.val)
        print(subRootRightDFS.val)
        print(TreeRightDFS.val)

        return (subRootLeftDFS.val == treeLeftDFS.val and subRootRightDFS.val == TreeRightDFS.val)
    
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