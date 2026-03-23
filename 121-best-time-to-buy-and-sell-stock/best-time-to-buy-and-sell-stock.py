class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # Step 1: update minimum price
            if price < min_price:
                min_price = price

            # Step 2: calculate profit
            profit = price - min_price

            # Step 3: update maximum profit
            if profit > max_profit:
                max_profit = profit

        return max_profit