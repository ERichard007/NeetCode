class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        mySet = set(nums)
        print(mySet)

        longestSequence = 0
        ct = 0
        lastNum = None
        for num in mySet:
            if lastNum == None: 
                lastNum = num
                ct += 1 
                longestSequence = max(ct, longestSequence)
                continue

            if num == lastNum+1:
                ct += 1
                lastNum = num
            else:
                ct = 0
            
            longestSequence = max(ct, longestSequence)

        return longestSequence

nums = [0,-1]

mySolution = Solution()
print(mySolution.longestConsecutive(nums))
