class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        slen = len(s)
        tlen = len(t)
        
        dp = [  [ -1 for col in range(tlen) ] for r in range(slen) ]
        
        def f(r, c):
            if c < 0: 
                return 1 
            if r < 0: 
                return 0
            if dp[r][c] != -1:
                return dp[r][c]
            
            if s[r] == t[c]:
                dp[r][c] =  f(r-1, c-1) + f(r-1, c)
                return dp[r][c] 
            else:
                dp[r][c] = f(r-1, c)
                return dp[r][c] 
        
        return f(slen-1, tlen-1)