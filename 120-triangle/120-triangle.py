class Solution:
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n = len(triangle) 
        dp = [ [ -1 for col in range(n) ] for r in range(n) ]
        def f(r,c):       
            if r == n-1:
                return triangle[r][c]

            if r < 0 or c < 0: 
                return float('inf') 

            if dp[r][c] != -1:
                return dp[r][c]

            down = triangle[r][c] + f(r+1,c)
            diag = triangle[r][c] + f(r+1, c+1)
            dp[r][c] = min(down, diag)
            return dp[r][c]  
        
        return f(0,0)
        