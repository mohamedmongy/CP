#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        #code here
        inf = int(1e8)
        dist = [inf] * V
        dist[S] = 0 
        
        for n in range(V):
            for e in edges:
                u  = e[0]
                v = e[1]
                wt = e[2]
                
                if dist[u] != inf and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
                    
        
        for e in edges: 
            u  = e[0]
            v = e[1]
            wt = e[2]
                
            if dist[u] != inf and dist[u] + wt < dist[v]:
                return [-1]
                
        return dist    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        edges = []
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            edges.append([u,v,w])
        S=int(input())
        ob = Solution()
        
        res = ob.bellman_ford(V,edges,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends