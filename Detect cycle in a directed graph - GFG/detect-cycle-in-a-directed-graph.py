#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        
        vis = [  0  for i in range(V) ]
        pathvis = [  0  for i in range(V) ]
        
        def dfs(v):
            vis[v] = 1 
            pathvis[v] = 1 
            
            for nbr in adj[v]:
                if vis[nbr] == 0: 
                    if dfs(nbr) == True: 
                        return True
                elif vis[nbr] == 1 and pathvis[nbr] == 1:
                    return True
                    
            pathvis[v] = 0
            return False         
            
            
        for v in range(V):
            if vis[v] == 0:
                if dfs(v) == True:
                    return True
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends