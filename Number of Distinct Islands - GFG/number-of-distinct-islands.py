#User function Template for python3

import sys
from typing import List


class Solution:
    sys.setrecursionlimit(10**8)
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        vis = [ [ 0  for _ in range(cols) ] for _ in range(rows) ]
        
        st = set()
        
        def dfs(r, c,tmp, orgr, orgc):
            vis[r][c] = 1
            tmp.append((r-orgr ,c -orgc))
            
            delr = [-1, 0, 1, 0]
            delc = [ 0, 1, 0, -1]
            
            for pos in range(4):
                nr = r + delr[pos]
                nc = c + delc[pos]
                
                if (nr >= 0 and
                nr < rows and
                nc >= 0 and
                nc < cols
                and grid[nr][nc] == 1
                and vis[nr][nc] == 0):
                    dfs(nr, nc, tmp, orgr, orgc)
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and vis[r][c] == 0:
                    tmp = []
                    dfs(r,c,tmp, r,c)
                    st.add(tuple(tmp))
                    
        return len(st)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends