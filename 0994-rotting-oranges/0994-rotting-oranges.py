
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        vis = [ [ 0  for c in range(cols)] for r in range(rows) ]
        q = deque()
        
        for cr in range(rows):
            for cc in range(cols):
                if grid[cr][cc] == 2:
                    q.append([cr,cc, 0])
                    vis[cr][cc] == 2 
        
        delr = [0, -1, 0, +1]
        delc = [-1, 0, +1, 0]
        tm = 0 
        
        def f():
            while(q):
                curr = q.popleft()
                r =  curr[0] 
                c =  curr[1]
                t =  curr[2]
                nonlocal tm
                tm = max(tm, t)
                
                for delta in range(4):
                    nr = r + delr[delta]
                    nc = c + delc[delta]
                    
                    if (nr >= 0 and
                        nr < rows and 
                        nc >= 0 and
                        nc < cols and
                        grid[nr][nc] == 1 and
                        vis[nr][nc] == 0):
                        vis[nr][nc] = 2
                        q.append([nr, nc, t+1] )
        
        f()
 
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and vis[i][j] != 2:
                    return -1
        
        return tm