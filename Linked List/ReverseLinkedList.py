from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        nextNode = None
        lastNode = None
        currentNode = head

        while (currentNode != None):
            nextNode = currentNode.next
            currentNode.next = lastNode
            lastNode = currentNode
            currentNode = nextNode

        return lastNode
        

mySolution = Solution()



head = [0,1,2,3]

myListNodeList = []
for n in range(len(head)):
    integer = head[n]
    nextNum = head[n+1] if n != len(head)-1 else None
    newListNode = ListNode(integer, nextNum)

    myListNodeList.append(newListNode)

for node in myListNodeList:
    print("val: " + str(node.val) + " next: " + str(node.next))

myNewListNodeList = mySolution.reverseList(myListNodeList[0])

for node in myNewListNodeList:
    print("val: " + str(node.val) + " next: " + str(node.next))