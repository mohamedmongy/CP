class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        rows = len(isConnected)
        cols = len(isConnected[0])
        
        adjl = [ [] for i in range(rows)]
        vis = [ False for i in range(rows)]

        def dfs(n):
            vis[n]  = True 
            
            for nei in adjl[n]:
                if not vis[nei]:
                    dfs(nei)
        
        for row in range(rows):
            for col in range(cols):
                if isConnected[row][col] == 1 and row != col:
                    adjl[row].append(col)
                    adjl[col].append(row) 
        
        cnt = 0 
        for v in range(rows):
            if not vis[v]:
                cnt += 1 
                dfs(v)
                
        return cnt 
        