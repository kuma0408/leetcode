class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        max_p = prices[-1]
        for i in range(len(prices)-1, -1, -1):
            max_p = max(max_p, prices[i])
            ans = max(ans, max_p - prices[i])

        return ans
