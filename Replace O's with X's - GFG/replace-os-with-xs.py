#User function Template for python3

class Solution:
    def fill(self, n, m, mat):
    
        vis   = [ [ 0 for _ in range(m) ] for _ in range(n) ]

        def dfs(r, c):
            vis[r][c] = 1 
            
            delr = [0, -1, 0, 1]
            delc = [-1, 0, 1, 0]
            
            for pos in range(4):
                nr = r + delr[pos]
                nc = c + delc[pos]
                
                if (nr >= 0 and
                nr < n and 
                nc >= 0 and
                nc < m and
                mat[nr][nc] == "O" and 
                vis[nr][nc] == 0):
                    dfs(nr, nc)
    
        # first row 
        for c in range(m):
            if mat[0][c] == "O" and vis[0][c] == 0:
                dfs(0, c)
                
        # last row 
        for c in range(m):
            if mat[n-1][c] == "O" and vis[n-1][c] == 0:
                dfs(n-1, c)    
        
        
         # first col 
        for r in range(n):
            if mat[r][0] == "O" and vis[r][0] == 0:
                dfs(r, 0)
                
         # last row 
        for r in range(n):
            if mat[r][m-1] == "O" and  vis[r][m-1] == 0:
                dfs(r, m-1)
        
        for rr in range(n):
            for cc in range(m):
                if mat[rr][cc] == "O" and vis[rr][cc] == 0: 
                    mat[rr][cc] = "X" 
          
        return mat 
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends