class Solution:
    def climbStairs(self, n: int) -> int:
        prev , prev2 = 1, 1
        
        for i in range(2,n+1):
            c = prev + prev2 
            prev2 = prev 
            prev = c
         
        return prev 
        