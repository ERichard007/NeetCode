from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if (len(stones) == 1):
            return stones[0]
        
        newList = sorted(stones,reverse=True)
        
        while(len(newList) > 1):
            print(newList)

            stone1 = newList.pop(0)
            stone2 = newList.pop(0)

            if (stone1 > stone2):
                stone1 -= stone2
                newList.append(stone1)
                newList.sort(reverse=True)
            elif (stone2 > stone1):
                stone2 -= stone1
                newList.append(stone2)
                newList.sort(reverse=True)

        print(newList)
        return (0 if len(newList) == 0 else newList[0])
    
stones = [2,3,6,2,4]
mySolution = Solution()

print(mySolution.lastStoneWeight(stones))