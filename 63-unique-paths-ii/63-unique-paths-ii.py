class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        rows =  len(obstacleGrid)
        cols = len(obstacleGrid[0])
        
        dp = [ [-1 for c in range(cols) ] for r in range(rows) ]
       
        def f(r,c,dp):
            
            if r >= 0 and c >= 0 and obstacleGrid[r][c] == 1:
                return 0 
            
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
            
        return f(rows-1, cols-1, dp)    
        