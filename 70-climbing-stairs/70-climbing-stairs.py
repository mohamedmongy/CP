class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [None]*(n+1)
        dp[0], dp[1] = 1 , 1  
        return self.climb(n, dp)
        
    def climb(self, n, dp):
        if dp[n]: 
            return dp[n]
    
        dp[n-1] = self.climb(n-1, dp) 
        dp[n-2] = self.climb(n-2, dp)
    
        return dp[n-1] + dp[n-2]