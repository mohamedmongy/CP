class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        
        lngth = len(nums)
        for i in range(1,lngth): 
            for j in range(0,i):
                # 9j 3j ... 7i
                if nums[i] > nums[j]:
                    dp[i]  = max(dp[i], dp[j]+1)
                    
        return max(dp)        
                
        
        