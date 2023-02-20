#User function Template for python3

from collections import deque
class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        res = []
        dq = deque() # ([f=0......b=-1])
        
        dq.append(0) # store idxs
        
        for i in range(1,k):
            while dq and arr[i] > arr[dq[-1]]:
                dq.pop()
            while dq and dq[0] <= (i - k):
                dq.popleft()
            dq.append(i)
        
        for lidx in range(k, n):
            res.append(arr[dq[0]])

            while dq and arr[lidx] > arr[dq[-1]]:
                dq.pop()
            
            while dq and dq[0] <= (lidx - k):
                dq.popleft()
                
            
            dq.append(lidx)
        res.append(arr[dq[0]])
            
        return res
    #     for i in range(n - k + 1):
    #         j =  i + k-1
    #         if j <= n and i <= j:
    #             subarr = arr[i:j+1]
    #             currmax = self.getmax(subarr)
    #             res.append(currmax)
    #         else: 
    #             break
    #     return res
       
    # def getmax(self, subarr):
    #     return max(subarr)
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends