class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # b_p = 0
        # b_flag = False
        # sum_v = 0
        # for i in range(len(prices) - 1):
        #     if prices[i] < prices[i + 1]:
        #         if b_flag == 0:
        #             b_flag = True
        #             b_p = prices[i]
        #         if i + 2 == len(prices):
        #             sum_v += prices[i+1] - b_p
        #     elif prices[i] >= prices[i + 1]:
        #         if b_flag == 0:
        #             continue
        #         else:
        #             sum_v += prices[i] - b_p
        #             b_p = 0
        #             b_flag = False
        # return sum_v

        profit = 0
        for i in range(1,len(prices)):
            if prices[i]-prices[i-1] > 0: 
                profit += (prices[i]-prices[i-1])
        return profit
        