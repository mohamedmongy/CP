class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [  -1 for j in range(n + 1 ) ]
        
        def f(i, k):
            if i == n:
                return 0 
            if dp[i] != -1:
                return dp[i]
            
            clen = 0
            cmaxi = float('-inf')
            
            maxans = float("-inf")
            
            for idx in range(i, min(n, i+k)):
                clen += 1
                cmaxi = max(cmaxi, arr[idx])
                csum = (clen * cmaxi) + f(idx+1,k)
                maxans = max(csum, maxans)
            dp[i] = maxans    
            return dp[i]
        
        return f(0, k)        
                
        