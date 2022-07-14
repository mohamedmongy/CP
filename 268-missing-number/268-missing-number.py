class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        
        dic = { i:i for i in nums }
        res = -1
        
        for val in range(length+1):
            if val not in dic:
                res = val
            
        return res     
        