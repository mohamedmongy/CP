#User function template for Python

class Solution:
	def shortest_distance(self, matrix):
		#Code here
		N = len(matrix[0])
		
		for r in range(N):
		    for c in range(N):
		        if matrix[r][c] == -1: 
		            matrix[r][c] = 1e8
		        if r == c:
		            matrix[r][c] = 0 
		
		for n in range(N):
		    for i in range(N):
		        for j in range(N):
		            matrix[i][j] = min(matrix[i][j] , matrix[i][n] + matrix[n][j])
		            
    	for r in range(N):
		    for c in range(N):
		        if matrix[r][c] == 1e8: 
		            matrix[r][c] = -1
   
        return matrix

#{ 
 # Driver Code Starts
#Initial template for Python 

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		obj.shortest_distance(matrix)
		for _ in range(n):
			for __ in range(n):
				print(matrix[_][__], end = " ")
			print()
# } Driver Code Ends