from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums)-1 #3
        low = 0 #2
        mid = int(len(nums)/2) #2

        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        while (mid < high and mid > low):
            if (target > nums[mid]):
                low = mid
                mid += int((high-low)/2)
            elif (target < nums[mid]):
                high = mid
                mid -= int((high-low)/2)
            elif (target == nums[mid]):
                return mid
        
        return -1

        

mySolution = Solution()

print(mySolution.search([-1,0,2,4,6,8], 3)) #should output 3