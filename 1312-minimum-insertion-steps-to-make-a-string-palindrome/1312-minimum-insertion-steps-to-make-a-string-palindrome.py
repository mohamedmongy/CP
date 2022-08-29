class Solution:
    def minInsertions(self, s: str) -> int:
                
        text1 = s 
        text2 = s[::-1]
        
        n1 = len(s)
        n2 = len(s)

        dp = [ [-1 for c in range(n2) ]  for r in range(n1) ]
        
        def f(idx1, idx2):
            
            if idx1 < 0 or idx2 < 0:
                return 0 
            
            if dp[idx1][idx2] != -1:
                return dp[idx1][idx2]
            
            if text1[idx1] == text2[idx2]:
                dp[idx1][idx2] = 1 + f(idx1-1, idx2-1)
                return dp[idx1][idx2]
            
            dp[idx1][idx2] =  max(f(idx1-1, idx2), f(idx1, idx2-1))
            return dp[idx1][idx2]
        
        return n1 - f(n1-1, n2-1)
        
        
        