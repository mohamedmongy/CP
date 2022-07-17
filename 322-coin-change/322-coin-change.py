class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0] = 0 
        
        for c in coins:
            for a in range(c,len(dp)):
                dp[a] = min(dp[a], dp[a-c]+1)
                
                
        return dp[amount] if dp[amount] <= amount else -1
            
        
   
        