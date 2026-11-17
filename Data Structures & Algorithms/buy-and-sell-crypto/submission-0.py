class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m,n = 0,0
        profit = 0

        while n != len(prices):
            if prices[m] <= prices[n]:
                profit = max(profit,(prices[n] - prices[m]))
                n += 1
            elif prices[m] > prices[n]:
                m += 1
        return profit

