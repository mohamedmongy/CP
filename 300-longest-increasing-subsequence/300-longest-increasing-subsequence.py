class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        #dp = [ [ 0  for c in range(n+1) ] for r in range(n+1) ]

        dp = [ 1 for i in range(n) ]
        res = [ i for i in range(n) ]
        
        def ft():
            # nums[ 4, 7, 11, 6]
            # res [ 0, 0, 1, ]
            
            lis = 1 
            lastidx = 0 
            
            for cidx in range(n):
                for pidx in range(cidx):
                    if nums[cidx] > nums[pidx] and (1 + dp[pidx]) > dp[cidx] :
                        dp[cidx] = 1 + dp[pidx]
                        res[cidx] = pidx
                
                if dp[cidx] > lis:
                    #lis = dp[cidx]
                    lastidx = cidx
                    
                lis = max(lis, dp[cidx])  
                
                temp = []
                
                while lastidx != res[lastidx]:
                    temp.append(nums[lastidx])
                    lastidx = res[lastidx]
                                    
            return lis                   
       
        def f(cidx, pidx):
            
            if cidx >= n:
                return 0 
            
            if dp[cidx][pidx+1] != -1:
                return  dp[cidx][pidx+1]
            
            tlen = 0 
            if pidx == -1 or nums[cidx] > nums[pidx]:
                tlen = 1 + f(cidx+1, cidx)
            
            ntlen = 0 + f(cidx+1, pidx)
            
            dp[cidx][pidx+1] = max(tlen, ntlen)
            return dp[cidx][pidx+1]
        
        
        return ft()
        
        