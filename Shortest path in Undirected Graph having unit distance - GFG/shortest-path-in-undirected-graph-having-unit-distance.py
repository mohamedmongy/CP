#User function Template for python3
from collections import deque 

class Solution:
    def shortestPath(self, edges, n, m, src):
        adj = [ [] for _ in range(n)]  
        
        for edg in edges:
            adj[edg[0]].append(edg[1])
            adj[edg[1]].append(edg[0])
       
        dist = [  float('inf') for _ in range(n) ]
        dq = deque()
        dist[src] = 0 
        dq.append((src, 0))
        
        def bfs(): 
            while dq:
                currnodetup = dq.pop()
                currnodeval = currnodetup[0]
                currnodedist = currnodetup[1]
                for nei in adj[currnodeval]: 
                    neinewdist = currnodedist + 1
                    if neinewdist < dist[nei]:
                        dist[nei] = neinewdist
                        dq.append((nei, neinewdist))

        bfs()
        
        for (idx, val) in enumerate(dist): 
            if val == float('inf'):
                dist[idx] = -1
            
        return dist


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends