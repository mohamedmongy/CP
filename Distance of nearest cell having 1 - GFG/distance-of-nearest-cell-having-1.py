
from  collections import deque 

class Solution:

    #Function to find distance of nearest 1 in the grid for each cell.
	def nearest(self, grid):

		rows = len(grid)
		cols = len(grid[0])
		
		vis = [ [ 0  for _ in range(cols) ] for _ in range(rows) ]
		dis = [ [ 0  for _ in range(cols) ] for _ in range(rows) ]
		
		dq = deque()
		
		for i in range(rows):
		    for j in range(cols):
		        if grid[i][j] == 1: 
		            dq.append([i, j , 0])
		            vis[i][j] = 1
		            dis[i][j] = 0

		def bfs():
		    
		    delr = [0, -1, 0, 1]
		    delc = [-1, 0, 1, 0]
		    
		    while dq:
		        curr = dq.popleft()
		        r = curr[0]
		        c = curr[1]
		        cost = curr[2]
		        
		        for deli in range(4):
		            nr =  r + delr[deli]
		            nc = c + delc[deli]
		            
		            if(nr >= 0 and
		            nr < rows and
		            nc >= 0 and
		            nc < cols and 
		            vis[nr][nc] == 0):
		                newcost = cost + 1
		                dq.append([nr, nc, newcost])
		                vis[nr][nc] = 1 
		                dis[nr][nc] =  newcost
  
        bfs()		    
		
		return dis
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		    


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.nearest(grid)
		for i in ans:
			for j in i:
				print(j, end = " ")
			print()

# } Driver Code Ends