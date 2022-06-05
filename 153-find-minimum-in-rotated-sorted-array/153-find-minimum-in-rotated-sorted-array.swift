class Solution {
    func findMin(_ nums: [Int]) -> Int {
        
        var count = nums.count 
        var lidx = 0 
        var ridx =  count-1 
        
        var pivot = 0 
        
        // try to know where is the bivot 
        
        for i in 0..<count { 
             if  i+1 < count && nums[i] <  nums[i+1]  {
                continue
            } else {
                if i == ridx {
                    break
                }
                
                pivot = i
                break
            }
        }
       
        
         
        lidx = pivot
       
        // search for the min element
        
        let arr = Array(nums[lidx...])
        return  arr.min()!
        
        
    }
}