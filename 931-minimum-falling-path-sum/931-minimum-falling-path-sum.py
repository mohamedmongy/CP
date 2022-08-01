class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        dp = [  [ -1 for c in range(cols)] for r in range(rows)]
        
        mini = float('inf')
            
        def f(r,c,dp):
            if c < 0 or c >= cols:
                return float('inf')
            
            if r == rows-1:
                return matrix[r][c]
            
            if dp[r][c] != -1:
                return dp[r][c]
            
            dgl = matrix[r][c] + f(r + 1, c - 1,dp)
            left = matrix[r][c] + f(r + 1, c,dp)
            dgr = matrix[r][c] + f(r + 1, c + 1,dp)
            
            dp[r][c] = min(dgl, min(left, dgr))
            
            return dp[r][c]
            
            
        for c in range(cols):
            mini = min(mini, f(0, c,dp))    
        
        return mini 
            
        
        