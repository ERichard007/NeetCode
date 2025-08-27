from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l,r = 0, 1

        while(r < len(prices)):
            if (prices[l] >= prices[r]):
                l = r
            else:
                profit = max(prices[r] - prices[l], profit)

            r += 1


        return profit

mySolution = Solution()

prices = [1,4,2]
print(mySolution.maxProfit(prices))