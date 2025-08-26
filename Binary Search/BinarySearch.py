from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if (nums[0] == target):
                return 0
            else:
                return -1


        high = len(nums)-1 #3
        low = 0 #2
        mid = low + int((high-low)/2)

        while (low <= high):
            print("high: ", nums[high], " low: ", nums[low], " mid: ", nums[mid])

            if (nums[mid] < target):
                low = mid+1
                mid = low + int((high-low)/2)
            elif (nums[mid] > target):
                high = mid-1
                mid = low + int((high-low)/2)
            elif (target == nums[mid]):
                return mid
        
        print("high: ", nums[high], " low: ", nums[low], " mid: ", nums[mid])
        return -1

        

mySolution = Solution()
nums=[-1,0,2,4,6,8]
target=3
print(mySolution.search(nums, target)) 