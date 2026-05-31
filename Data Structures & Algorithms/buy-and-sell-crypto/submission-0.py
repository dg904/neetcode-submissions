class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_left = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > min_left and prices[i]-min_left >profit:
                profit = prices[i] - min_left
            elif prices[i]<min_left:
                min_left = prices[i]                
        return profit