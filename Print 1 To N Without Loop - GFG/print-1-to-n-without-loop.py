#User function Template for python3

class Solution:    
    #Complete this function
    def printNos(self,N):
        def f(i): 
            if i > N: 
                return 
            print(i, end =" ")
            f(i+1)
        f(1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        ob=Solution()
        
        ob.printNos(N)
        print()
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends