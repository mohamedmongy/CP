class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstr = str(x)
        xlen = len(xstr)
        l = 0 
        r = xlen-1
        
        while l <= r:
            if xstr[l] != xstr[r]:
                return False 
            l += 1 
            r -= 1 
       
        return True 
        