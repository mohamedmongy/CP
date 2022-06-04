class Solution {
    func maxProduct(_ nums: [Int]) -> Int {
        
        
        var currMax = 1 
        var currMin = 1 
        var res = nums.max()!
        
        
        for num in nums {  
           
            if num == 0 { 
                currMin = 0 
                currMax = 0
                continue 
            }
            
           let tmpMax = num * currMax
           let  tmpMin = num * currMin 
            
            currMax = max(tmpMax, max(tmpMin, num))
            currMin = min(tmpMax, min(tmpMin, num)) 
            
            res = max(res, max(currMax, currMin))
        }
        
        return res   
        
    }
}