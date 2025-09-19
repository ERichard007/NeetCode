from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        
    def add(self, val: int) -> int:
        stack = []
        heapq.heappush(self.nums,val)
        heap = self.nums[:]

        for i in range(len(heap)):
            stack.append(heapq.heappop(heap))
            
        return stack.pop(-self.k)

list = [1, 2, 3, 3]
myClass = KthLargest(3, list)
myClass.add(3);   # return 3
myClass.add(5);   # return 3
myClass.add(6);   # return 3
myClass.add(7);   # return 5
myClass.add(8);   # return 6
