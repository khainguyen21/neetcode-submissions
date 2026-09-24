class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0 , 1
        maxProfit = 0 
        while r < len(prices):
            if prices[r] - prices[l] < 0: 
                l = r

            elif r == len(prices) - 1:
                maxProfit += (prices[r] - prices[l])
 
            elif prices[r] > prices[r+1]:
                maxProfit += (prices[r] - prices[l])
                l = r + 1
                r = l

            r += 1
        
        return maxProfit

    
        