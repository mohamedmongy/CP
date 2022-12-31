#User function Template for python3

from queue import PriorityQueue

class Solution:
    def shortestPath(self, n, m, edges):
        # [ (node, distance)] 
        # - - - - - - - 
        adj = [ [] for _ in range(n+2) ] 
        
        for edge in edges:
            f = edge[0]
            t = edge[1]
            w = edge[2]
            adj[f].append((t,w))
            adj[t].append((f,w))
        
        pq = PriorityQueue() 
        dist = [ float('inf') for _ in range(n+2) ]
        parent = [ i for i in range(n+2) ]
        dist[1] = 0 
        
        pq.put([0, 1])
        
        while not pq.empty():
            currdist, currnode = pq.get()
            nbrs = adj[currnode]

            for nbr in nbrs: 
                nbrnode = nbr[0]
                nbrcost = nbr[1]
                
                if currdist + nbrcost < dist[nbrnode]: 
                    dist[nbrnode] = currdist + nbrcost
                    parent[nbrnode] = currnode
                    pq.put(( currdist + nbrcost, nbrnode))
        
        res = [] 
        if dist[n] == float('inf'):
            res.append(-1)
            return res 
        
        node = n
        while parent[node] != node: 
            res.append(node)
            node = parent[node]
        res.append(1)
        return res[::-1]
            
         


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        edges = []
        for i in range(m):
            node1, node2, weight = list(map(int, input().split()))
            edges.append([node1, node2, weight])
        obj = Solution()
        ans = obj.shortestPath(n, m, edges)
        for e in ans:
            print(e, end = ' ')
        print()
# } Driver Code Ends