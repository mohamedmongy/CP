
from collections import deque 

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        
        indegress = [ 0 for _ in range(V) ]
        for v in range(V):
            for n in adj[v]: 
                indegress[n] += 1

        dq = deque()
        for v in range(V): 
            if indegress[v] == 0:
                dq.append(v)
                
        res = []
        
        while dq:
            node = dq.pop()
            res.append(node)
            
            for nbr in adj[node]:
                indegress[nbr] -= 1 
                if indegress[nbr] == 0: 
                    dq.append(nbr)
            
        return res
        # vis = [ 0 for _ in range(V) ]
        # stk = []
        
        # def dfs(n):
        #     vis[n] = 1 
        #     for nbr in adj[n]:
        #         if vis[nbr] == 0: 
        #             dfs(nbr)
        #     stk.append(n)
            
            
        # for n in range(V):
        #     if vis[n] == 0: 
        #         dfs(n)
        # return stk[::-1]



#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends