#User function Template for python3

class Solution:
    def printNos(self, n):
        # Code here
        def f(i): 
            if i < 1: 
                return 
            print(i, end =" ")
            f(i-1)
        f(n)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printNos(N)
        print()
# } Driver Code Ends