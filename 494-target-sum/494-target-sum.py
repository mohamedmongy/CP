class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)

        dp = [ [ -1  for t in range(2*total+1) ] for r in range(n)]
        
        def f(idx,cursum,target):
            if idx < 0 and target == cursum: 
                return 1 
            
            if idx < 0 and target != cursum:
                return 0
            
            if dp[idx][cursum + total] != -1: 
                return dp[idx][cursum+ total]
              
            take = f(idx-1, cursum + nums[idx], target)
            nottake = f(idx-1, cursum +(-nums[idx]) , target)
            
            dp[idx][cursum+ total] =  take + nottake 
            return dp[idx][cursum + total]
        
        
        return f(n-1, 0, target)
            
        
        