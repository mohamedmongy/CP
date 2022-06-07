class Solution {
    func maxArea(_ height: [Int]) -> Int {
        var res = 0 
        var left = 0
        var right = height.count - 1
        
        
        while left < right {
            let area = (right - left) * min(height[left], height[right])
            res = max(res , area)
            
            if height[left] < height[right] {
                left += 1
            } else {
                right -= 1
            }
        }
 
        
        return res
        
    }
}