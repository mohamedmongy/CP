

from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here

		q = deque() 
		vis = [ 0  for i in range(V) ]
	    
	    def f(src):	
    		q.append([src, -1])
    		vis[src] = 1 
    		
    		while q: 
    		    curr = q.popleft()
    		    s = curr[0]
    		    p = curr[1]
    		    candts = adj[s]
    		    
    		    for candt in candts:
    		        if vis[candt] == 0: 
    		            q.append([candt, s])
    		            vis[candt] = 1 
    		        else:
    		            if p != candt:
    		                return 1
    		return 0  
    		
		for node in range(V):
		    if vis[node] == 0:
		        if f(node):
		            return 1 
		return 0         

		
		


#{ 
 # Driver Code Starts


if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends