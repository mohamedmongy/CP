class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        dp = [ [ -1 for c in range(amount+1) ] for r in range(n)]
        
        def f(idx, t):
            if t == 0: 
                return 1 
            
            if idx < 0:
                return 0
            
            if dp[idx][t] != -1:
                return dp[idx][t]
            
            nottake = 0 + f(idx-1, t)
            
            take = 0
            if t >= coins[idx]:
                take = f(idx, t-coins[idx])
            
            dp[idx][t] = take + nottake
            return dp[idx][t]
        
        return f(n-1, amount)
        
        
        
        
        