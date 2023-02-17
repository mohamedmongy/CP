#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s):
        res = []
        
        lft = 0 
        currsum = arr[0]
        rgt = 1 
        
        while rgt <= n:
            while currsum > s and lft < rgt-1:
                currsum -= arr[lft]
                lft += 1
            
            if currsum == s:
                res.append([lft+1, rgt])
                return res[0]
            
            if rgt < n:
                currsum += arr[rgt]
            rgt += 1
            
        res.append([-1])    
        return res[0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends