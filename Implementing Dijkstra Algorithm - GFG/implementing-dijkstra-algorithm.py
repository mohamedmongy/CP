from queue import PriorityQueue


#  [ [1, _] , [2, _ ] ] 
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        dist = [ float('inf') for n in range(V) ]
        dist[S] = 0 
        q = PriorityQueue()
        q.put((0, S))
        
        while not q.empty():
            currdist, currnode = q.get()
            nbrs = adj[currnode]

            for nbr in nbrs: 
                nbrnode = nbr[0]
                nbrcost = nbr[1]
                
                if currdist + nbrcost < dist[nbrnode]: 
                    dist[nbrnode] = currdist + nbrcost
                    q.put(( currdist + nbrcost, nbrnode))
            
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
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends