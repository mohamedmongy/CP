class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [ [-1 for c in range(n) ] for r in range(m) ]
       
        def f(r,c,dp):
            if r == 0 and c == 0: 
                return 1 
            
            if r < 0 or c < 0:
                return 0 
            
            if dp[r][c] != -1: 
                return dp[r][c]
            
            left = f(r, c-1,dp)
            up = f(r-1, c,dp)
            
            dp[r][c] = left + up 
            
            return dp[r][c]
            
        return f(m-1, n-1, dp)    
        