class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        slen = len(s)
        plen = len(p)
        
        dp = [ [ -1 for c in range(plen)] for i in range(slen)]
        
        def f(i, j):
            
            if i< 0 and j < 0:
                return True
            
            if i < 0 and j >= 0:
                for currj in range(j+1):
                    if p[currj] != '*':
                        return False 
                return True        
            
            if j < 0 and i >= 0: 
                return False 
             
            if dp[i][j] != -1:
                return dp[i][j]
            
            if p[j] == s[i] or p[j] == '?':
                dp[i][j] = f(i-1, j-1)
                return dp[i][j]
            
            if p[j] == '*':
                dp[i][j] = f(i, j-1) or f(i-1, j)
                return dp[i][j]
            
            return False 
        
        return f(slen-1, plen-1)
            
            
        