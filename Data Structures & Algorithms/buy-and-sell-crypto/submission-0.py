class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_price = prices[0]
        n = len(prices)

        for i in range(1, n):
            min_price = min(min_price, prices[i])
            ans = max(ans, prices[i] - min_price)

        return ans