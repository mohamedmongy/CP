class Solution {
    func threeSum(_ nums: [Int]) -> [[Int]] {
        
        var res: [ [ Int] ] = []
        var  nums = nums
        nums.sort()
        var s = 0 
        var e = 0 
        
        for c in 0..<nums.count {
            
            var s = c + 1 
            var e  = nums.count - 1
            
            // don't take the repeated value 
            if c > 0 {
                if nums[c] == nums[c-1] {
                    continue 
                }
            }
          
        
            while  s < e   {
                let target =  nums[c] * -1 
                
                let currSum =  nums[s] + nums[e]
                
                if currSum == target {
                    res.append([nums[c], nums[s], nums[e]])  
                    s = s + 1 
                    
                   while nums[s] == nums[s-1] &&   s < e   {
                        s = s + 1 
                   }
                } else if  currSum > target {
                    e = e - 1 
                } else { 
                    s = s + 1 
                }
           
                
            }  
        }
       
       return res 
      
    }
}