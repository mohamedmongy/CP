class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        l = 0 
        r = N - 1
        res = X
        residx = -1
        while l <= r: 
            mid = int((l+r) / 2)
            if A[mid] == X: 
                return mid
            elif X > A[mid]:
                res = min(A[mid], res)
                residx = mid
                l = mid + 1 
            else:
                if A[mid] < res:
                    residx = mid
                    break
                r = mid - 1
        return residx
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            NX=[int(x) for x in input().strip().split()]
            N=NX[0]
            X=NX[1]

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            print(obj.findFloor(A,N,X))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends