class Solution {
    func productExceptSelf(_ nums: [Int]) -> [Int] {
         var res = Array.init(repeating: 1, count: nums.count)
          
        // [1,2,3,4]
         
        let count = nums.count 
        
         var prefix = 1 
        
        for  lidx in 0..<count { 
            res[lidx] = prefix 
            prefix = prefix * nums[lidx]
        }
        
        var postfix = 1 
        
        for (lidx,val) in nums.enumerated().reversed() { 
            res[lidx] = res[lidx] * postfix 
            postfix = postfix * nums[lidx]
        } 
        

          
           
          return res
    }
}