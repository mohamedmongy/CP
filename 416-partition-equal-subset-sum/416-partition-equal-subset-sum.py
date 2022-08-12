class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        mod = total%2
        n = len(nums)
        target = total // 2
        
        if mod > 0:
            return False
        
        dp = [  [ -1 for t in range(target+1) ] for r in range(n) ] 
        
        def f(idx, target):
            if target == 0: 
                return True
            
            if idx == 0:
                return nums[idx] == target
            
            if dp[idx][target] != -1:
                return dp[idx][target]
                
            take = False 
            if target > nums[idx]:
                take = f(idx-1, target-nums[idx])
            nottake =  f(idx-1, target)
            dp[idx][target] = take or nottake 
            
            return dp[idx][target]
        
        
        return f(n-1, target)
        
       