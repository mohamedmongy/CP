class Solution:
    
    def longestConsecutive(self, nums: List[int]) -> int:
        count = set(nums) #{ n:0 for n in nums }
     
        res = 0 
        
        for n in nums:
            lnght = 0 
            if n -1 not in count:
                while n + lnght in count:
                    lnght += 1 
                res = max(res, lnght)    
            
        return res 