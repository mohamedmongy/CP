class Solution:
	def isBipartite(self, V, adj):
		#code here
		
		colors = [ -1 for c in range(V) ]
		
		def dfs(curr, col): 
            colors[curr] = col 
            
            for nbr in adj[curr]: 
                if colors[nbr] == -1: 
                    if dfs(nbr, not col) == False:
                        return False
                elif colors[nbr] == col:
                    return False
                    
            return True
            
		for i in range(V):
		    if colors[i] == -1:
		        if dfs(i, 0) == False: 
		            return False
        return True 
        
        
            

#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends