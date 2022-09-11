class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        w1len = len(word1)
        w2len = len(word2)
        
        dp = [ [ -1 for c in range(w2len) ] for r in range(w1len)]
        
        def f(i,j):
            if i < 0:
                return j + 1
            
            if j < 0: 
                return i + 1 
            
            if dp[i][j] != -1:
                return dp[i][j]
                
            if word1[i] == word2[j]: 
                dp[i][j] = 0 + f(i-1, j-1)
                return dp[i][j]
            else:
                dp[i][j] = min(min( 1 + f(i-1,j),  1 + f(i, j-1)) , 1 + f(i-1,j-1))
                return dp[i][j]
            
        return f(w1len-1, w2len-1)
        