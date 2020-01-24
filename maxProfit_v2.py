class Solution:
    def maxProfit(self, prices: [int]) -> int:
        max_profit = 0
        if len(prices) <= 1:
            return 0
        low = prices[0]
        for day in range(1, len(prices)):
            if low > prices[day]:
                low = prices[day]
            if prices[day] > prices[day-1]:
                if prices[day] - low > max_profit:
                    max_profit = max_profit + (prices[day] - low)
        return max_profit


prices = [7,1,5,3,6,4]
#print(prices[1:2])
print(Solution().maxProfit(prices))
