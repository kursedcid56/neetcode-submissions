class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        max_profit = 0
        while r < len(prices):
           if price[r] - prices[l] > 0:
            max_profit = max(max_profit,prices[r]-prices[l])
            r+=1
           else:
            l = r
        return max_profit     