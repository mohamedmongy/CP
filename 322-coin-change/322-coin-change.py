class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [ [ -1 for c in range(amount+1) ] for r in range(n)]
        maxi = float('inf')
        
        def f(idx, t):
            if t == 0: 
                return 0 
            
            if idx < 0:
                return maxi
            
            if dp[idx][t] != -1:
                return dp[idx][t]
            
            nottake = f(idx-1, t)
            
            take = maxi
            if t >= coins[idx]:
                take = 1 + f(idx, t-coins[idx])
            
            dp[idx][t] = min(take, nottake)
            return dp[idx][t]
        
        res = f(n-1, amount)
        
        if res != maxi:
            return res
        return -1
   
        