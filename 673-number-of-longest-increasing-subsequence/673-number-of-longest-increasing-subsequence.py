class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [ 1 for i in range(n) ]
        cnt = [ 1 for i in range(n) ] 
        
        lis = 1 
        
        for cidx in range(n):
            for pidx in range(cidx):
                if nums[cidx] > nums[pidx] and (dp[pidx] + 1) > dp[cidx]: 
                    dp[cidx] = dp[pidx] + 1
                    cnt[cidx] = cnt[pidx]
                elif nums[cidx] > nums[pidx] and dp[cidx] == (dp[pidx] + 1) :
                    cnt[cidx] += cnt[pidx]
            lis = max(lis, dp[cidx])
            
        num = 0
        for i in range(n):
            if dp[i] == lis:
                num += cnt[i]
        return num
        