class Solution:
	def isBipartite(self, V, adj):
		colors = [ -1 for c in range(V) ]
		
		def dfs(curr, col): 
            colors[curr] = col 
            res = True
            for nbr in adj[curr]: 
                if colors[nbr] == -1: 
                    res = res and dfs(nbr, not col)
                elif colors[nbr] == col:
                    res =  res and False
            return res
        
        res = True
		for i in range(V):
		    if colors[i] == -1:
		        res = res and dfs(i, 0)
        return res 
        
        
            

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