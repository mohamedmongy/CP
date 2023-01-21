#User function Template for python3
from queue import PriorityQueue

class Solution:
        
    def MinimumEffort(self, a):
        rows = len(a)
        cols = len(a[0])
        pq = PriorityQueue() 
        dist = [ [ float('inf') for _ in range(cols) ]  for _ in range(rows) ]
       
        dist[0][0] = 0 
        
        # (diff , [r, c])
        pq.put((0, [0, 0]))
        
        while not pq.empty():
            currdiff, point = pq.get()
            curr = point[0]
            curc = point[1]
            
            if curr == rows -1 and curc == cols - 1:
                return currdiff 
            
            delr = [-1, 0 ,1 , 0]
            delc = [ 0, 1, 0, -1]
            
            for idx in range(4):
                newr = curr + delr[idx]
                newc = curc + delc[idx]
                
                if newr >= 0 and newr < rows and newc >= 0 and newc < cols: 
                    newdiff =  max( abs(a[curr][curc]  - a[newr][newc]), currdiff)
                    if newdiff < dist[newr][newc]: 
                        dist[newr][newc] = newdiff
                        pq.put((newdiff, [newr, newc]))
                
        return 0 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n,m=map(int,input().split())
        a=[]
        for i in range(n):
            li=list(map(int,input().split()))
            a.append(li)
        ob = Solution()
        ans = ob.MinimumEffort(a)
        print(ans)
        tc -= 1
# } Driver Code Ends