class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # n = len(prices)  #Bruteforce Approach
        # maxProfit = 0
        # for i in range (0,n):
        #     for j in range (i+1,n):
        #         profit = prices[j]-prices[i]
        #         maxProfit = max(maxProfit,profit)
        # return maxProfit

        max_profit = 0
        min_price = float("inf")
        n = len(prices)
        for i in range (0,n):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i]-min_price)
        return max_profit