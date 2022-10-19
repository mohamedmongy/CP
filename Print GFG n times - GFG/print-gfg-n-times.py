#User function Template for python3

class Solution:
    def printGfg(self, n):
        # Code here
        
        def f(i):
            if i == n:
                return 
            print("GFG", end =" ")
            f(i+1)
        f(0)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printGfg(N)
        print()
# } Driver Code Ends