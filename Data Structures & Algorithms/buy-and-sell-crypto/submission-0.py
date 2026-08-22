class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        p1 = 0
        p2 = 1

        while p2 < len(prices):
            if prices[p2] - prices[p1] < 0:
                p1 = p2
            else:
                profit = max(prices[p2] - prices[p1], profit)
            p2 += 1
        return profit