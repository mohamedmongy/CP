class Solution {
   func search(_ nums: [Int], _ target: Int) -> Int {
        // return bs(nums, target, res: nums)
       
        var l = 0
        var r = nums.count-1
        
        while l <= r {
            let mid = (l+r)/2
            
            if nums[mid] == target {
                return mid
            } else if nums[mid] < target {
                l = mid+1
            } else {
                r = mid-1
            } 
        }
        
        return -1
     }
}
    
//       func bs(_ nums: [Int], _ target: Int, res: [Int]) -> Int {
        
//         if !nums.isEmpty {
//             let mid = nums.count / 2
            
//             // check the mid is the target
//             if nums[mid] == target {
//                 return res.firstIndex(of: target) ?? -1
//             }
            
//             // take the left part
//             if nums[mid] > target {
//                 let leftArr  = Array(nums[0..<mid])
//                 return  bs(leftArr, target, res: res)
//             } else {
//                 let rightArr = Array(nums[mid+1..<nums.count])
//                 return  bs(rightArr, target, res: res)
//             }
//         } else {
//             return -1
//         }
// }