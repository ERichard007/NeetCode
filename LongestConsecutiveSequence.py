class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        mySet = set(nums)

        longestSequence = 0
        for num in nums:
            length = 0
            while (num + length) in mySet:
                length+=1
            longestSequence = max(longestSequence, length)

        return longestSequence

nums = [2,20,4,10,3,4,5]

mySolution = Solution()
print(mySolution.longestConsecutive(nums))
