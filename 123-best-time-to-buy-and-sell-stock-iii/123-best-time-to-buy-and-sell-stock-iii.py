class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        n = len(prices)
        capT = 3 
        buy = 2
        
        dp = [ [ [ 0  for c in range(capT) ] for p in range(2) ] for r in range(n+1) ]
        
        def f(idx, canBuy,cap):
            if idx >= n:
                return 0 
            
            if cap == 0:
                return 0
            
            if dp[idx][canBuy][cap] != -1:
                return dp[idx][canBuy][cap]
            
            profit = 0 
            if canBuy:
                profit = max(-prices[idx] + f(idx+1, 0,cap), f(idx+1, 1,cap))
            else:
                profit = max(+prices[idx] + f(idx+1, 1, cap-1), f(idx+1, 0,cap))
                
            dp[idx][canBuy][cap] = profit
            return dp[idx][canBuy][cap]
        
        def ft():
            for idx in range(n-1,-1,-1):
                for canBuy in range(buy):
                    for cap in range(1,capT,1):
                        if canBuy:
                            dp[idx][canBuy][cap] = max(-prices[idx] + dp[idx+1][0][cap], dp[idx+1][1][cap])
                        else:
                            dp[idx][canBuy][cap] = max(+prices[idx] + dp[idx+1][1][cap-1], dp[idx+1][0][cap])
                            
            return dp[0][buy-1][capT-1]
        
        return ft()
        