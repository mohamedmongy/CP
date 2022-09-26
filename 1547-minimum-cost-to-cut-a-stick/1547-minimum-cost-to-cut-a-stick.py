class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(n)
        cuts.insert(0,0)
        cuts.sort()
        c = len(cuts)

        dp = [ [-1 for c in range(c) ] for i in range(c) ]
        def f(start, end):
            if start > end:
                return 0 
            
            if dp[start][end] != -1:
                return dp[start][end]
            
            mini = float('inf')
            for idx in range(start, end+1):
                cost =  (cuts[end+1] - cuts[start-1]) + f(start, idx-1) + f(idx+1, end)
                mini = min(mini, cost)
                dp[start][end] = mini
                
            return dp[start][end]    
        return f(1, c-2)
            
        