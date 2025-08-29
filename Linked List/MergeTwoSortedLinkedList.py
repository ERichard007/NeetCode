from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None: return list2
        elif list2 == None: return list1

        currentNode = list1 if list1.val <= list2.val else list2
        currentExchangeNode = list2 if currentNode == list1 else list1
        newHead = currentNode

        while (currentNode.next != None and currentExchangeNode != None):
            if (currentExchangeNode.val <= currentNode.next.val): #inser the new node because it is greater than the last and less than the next
                tempNode = currentExchangeNode.next
                currentExchangeNode.next = currentNode.next
                currentNode.next = currentExchangeNode
                currentExchangeNode = tempNode
            else:
                currentNode = currentNode.next
        
        if (currentExchangeNode != None):
            currentNode.next = currentExchangeNode


        return newHead
    
mySolution = Solution()

listNode3 = ListNode(4)
listNode2 = ListNode(2,listNode3)
listNode1 = ListNode(1,listNode2)

bListNode3 = ListNode(5)
bListNode2 = ListNode(3,bListNode3)
bListNode1 = ListNode(1,bListNode2)

headOfSortedLinkedList = mySolution.mergeTwoLists(listNode1, bListNode1)

nextNode = headOfSortedLinkedList.next
print(headOfSortedLinkedList.val)
while nextNode != None:
    print(nextNode.val)
    nextNode = nextNode.next

