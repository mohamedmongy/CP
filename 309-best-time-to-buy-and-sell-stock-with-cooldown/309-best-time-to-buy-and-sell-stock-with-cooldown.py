class Solution:
    def maxProfit(self, prices: List[int]) -> int:
               
        n = len(prices)
        
        dp = [ [ -1 for c in range(2)] for r in range(n) ]
        
        def f(idx, canBuy):
            if idx >= n:
                return 0 
            
            if dp[idx][canBuy] != -1:
                return dp[idx][canBuy]
            
            profit = 0 
            if canBuy:
                profit = max(-prices[idx]  + f(idx+1, 0), f(idx+1, 1))
                dp[idx][canBuy] = profit
            else:
                profit = max(+prices[idx] + f(idx+2, 1), f(idx+1, 0))
                dp[idx][canBuy]
            dp[idx][canBuy] = profit
            return dp[idx][canBuy]              
        
        return f(0, 1)
        