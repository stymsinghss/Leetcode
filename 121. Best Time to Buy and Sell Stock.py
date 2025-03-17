from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0

        for right in range(len(prices)):
            if prices[right] > prices[left]:
                # we can make profit
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right
        return max_profit
