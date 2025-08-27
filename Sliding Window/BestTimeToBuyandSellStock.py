from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for day in range(len(prices)-1):
            current_day_profit = prices[day]
            for other_days in range(day+1, len(prices)):
                hypothetical_profit = prices[other_days] - current_day_profit
                profit = max(hypothetical_profit, profit)


        return profit

mySolution = Solution()

prices = [10,8,7,5,2]
print(mySolution.maxProfit(prices))