class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        withoutfirst  = nums[1:n]
        withoutlast = nums[:n-1]
        l1 = len(withoutfirst)
        l2 = len(withoutlast)
        dp1 = [-1] * l1 
        dp2 = [-1] * l2 

        def f(idx, values ,dp):
            if idx == 0:
                return values[idx]
            if idx < 0:
                return 0 
            if dp[idx] != -1:
                return dp[idx]
            l = values[idx] + f(idx-2, values, dp)
            r =  0 + f(idx-1, values, dp)
            dp[idx] = max(l, r)
            return dp[idx]

        lres = f(l1-1, withoutfirst, dp1)
        rres = f(l2-1, withoutlast, dp2)   
        return max(lres, rres)

        