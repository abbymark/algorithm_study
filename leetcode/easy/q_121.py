class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## Time limit exceeded
        # mx_value = 0
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         if prices[j] - prices[i] > mx_value:
        #             mx_value = prices[j] - prices[i]
        # return mx_value

        min_price = prices[0]
        max_val = 0
        for p in prices:
            max_val = max(max_val, p - min_price)
            min_price = min(min_price, p)
        return max_val