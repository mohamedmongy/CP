#User function Template for python3

from typing import List
from collections import deque 
class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        
        revadj = [ [] for _ in range(V)]
        indgrs = [ 0 for _ in range(V)]
        
        for s in range(V):
            for d in adj[s]:
                revadj[d].append(s)
                indgrs[s] += 1 
                
        
        dq = deque()
        
        for st in range(V):
            if indgrs[st] == 0:
                dq.append(st)
                
                
        safes = []
        
        while dq:
            cur = dq.pop()
            safes.append(cur)
            
            for nbr in revadj[cur]:
                indgrs[nbr] -= 1 
                if indgrs[nbr] == 0:
                    dq.append(nbr)
            
        
        # return safes        
                

        # vis = [ 0  for v in range(V)]
        # pathvis = [ 0  for v in range(V)]
        
        # res = [0  for v in range(V) ]
        
        # def dfs(n, res):
        #     vis[n] = 1 
        #     pathvis[n] = 1
        #     res[n] = 0 
            
        #     # allpathres = True
            
        #     for nbr in adj[n]:
        #         if vis[nbr] == 0:
        #             if dfs(nbr, res) == True:
        #                 res[n] = 0 
        #                 return True
        #         elif pathvis[nbr] == 1:
        #             # allpathres = allpathres and False
        #             res[n] = 0
        #             return True
                    
        #     res[n] = 1
        #     pathvis[n] = 0 
        #     return False
        
        # for n in range(V):
        #     if vis[n] == 0:
        #         dfs(n, res)
        
        # safe = []
        
        # for nd in range(V):
        #     if res[nd] == 1:
        #         safe.append(nd)
        
        return sorted(safes)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


# } Driver Code Ends