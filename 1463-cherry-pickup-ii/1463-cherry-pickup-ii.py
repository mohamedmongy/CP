class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        dp = [  [  [  -1 for c2 in range(cols) ] for c1 in range(cols) ] for r in range(rows) ]
        
        def f(r, c1, c2):
            if c1 < 0 or c1 >= cols or c2 < 0 or c2 >= cols:
                return float('-inf')
            
            if r == rows-1:
                if c1 == c2:
                    return grid[r][c1]
                else:
                    return grid[r][c1] + grid[r][c2]
            
            if dp[r][c1][c2] != -1:
                return dp[r][c1][c2]
            
            # how to monve both of the robot at the same time 
            
            maxi = float('-inf')
            
            for r1move in range(-1,2):
                for r2move in range(-1,2):
                    if c1 == c2: 
                        maxi = max(maxi,  grid[r][c1] + f(r+1, c1+r1move, c2+r2move))
                    else:
                        maxi = max(maxi, grid[r][c1] + grid[r][c2] + f(r+1, c1+r1move, c2+r2move))
                        
            dp[r][c1][c2] = maxi            
            return dp[r][c1][c2]         
            
        return f(0,0,cols-1)        
                
                
        