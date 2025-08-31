from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head.next == None or head.next.next == None: return False

        slowPointer = head
        fastPointer = head.next.next 

        while fastPointer != None:
            print("Slow: " + str(slowPointer.val) + " Fast: " + str(fastPointer.val))
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next if fastPointer.next != None else None

            if slowPointer == fastPointer:
                print("Slow: " + str(slowPointer.val) + " Fast: " + str(fastPointer.val))
                return True

        return False
    

mySolution = Solution()

listNode4 = ListNode(4)
listNode3 = ListNode(3,listNode4)
listNode2 = ListNode(2,listNode3)
listNode1 = ListNode(1,listNode2)

listNode4.next = listNode2

print(mySolution.hasCycle(listNode1))