class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_p = 0
        sell_p = 1
        lowest_buy = prices[0]
        while sell_p < len(prices):
            profit = prices[sell_p] - prices[buy_p]
            if profit > max_profit:
                max_profit = profit
            else:
                if prices[sell_p] < prices[buy_p]:
                    buy_p = sell_p
            sell_p += 1
        return max_profit
