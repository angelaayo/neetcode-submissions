class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profit = 0

        for right in range(1, len(prices)):
            if prices[left] > prices[right] and right!=len(prices)-1:
                left = right  #left index should become right
            else:
                profit = max(profit, prices[right] - prices[left])
        return profit
# 2 1 2 1 0 1 2    len = 7 
#         l   r
# profit = 2