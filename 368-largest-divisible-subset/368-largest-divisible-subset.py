class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        nums.sort() 
        
        dp = [ 1 for i in range(n) ] 
        previdx = [ j for j in range(n)] 
        
        lastidx = 0 
        lis = 1
        
        for cidx in range(n):
            for pidx in range(cidx):
                if nums[cidx] % nums[pidx] == 0 and (dp[pidx] + 1) > dp[cidx]: 
                    dp[cidx] = dp[pidx] + 1
                    previdx[cidx] = pidx
                    
            if dp[cidx] > lis:
                lis = dp[cidx]
                lastidx = cidx 
                
            lis = max(lis, dp[cidx])  
        
        temp = []
        
        while lastidx != previdx[lastidx]:
            temp.append(nums[lastidx])
            lastidx = previdx[lastidx]
 
        temp.append(nums[lastidx])       
        return temp