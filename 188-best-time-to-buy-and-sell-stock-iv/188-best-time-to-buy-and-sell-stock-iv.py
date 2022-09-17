class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        capT = k + 1  # 0 1 2 3 
        buy = 2 # 0 , 1 
        
        dp = [ [ [ 0  for c in range(capT) ] for p in range(2) ] for r in range(n+1) ]
        
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
        