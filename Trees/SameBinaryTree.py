from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            print("not q and p")
            return True
        elif not p or not q or p.val != q.val:
            print("not p or not q")
            return False
        
        print("ValP: " + str(p.val) + " ValQ: " + str(q.val) )
        
        isSame = self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)

        return(isSame)




mySolution = Solution()

tree1 = TreeNode(4,TreeNode(7))
tree2 = TreeNode(4,None,TreeNode(7))

print(mySolution.isSameTree(tree1,tree2))