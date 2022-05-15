class Solution {
    func subsets(_ nums: [Int]) -> [[Int]] {
        
        var res: [[Int]] = []
        var input: [Int] = []
        
        sol(input: &input, idx: 0, org: nums, output: &res)

        return res
    }
      
    // 01 , 0 , []
    // 0  1
    
  func sol(input: inout [Int], idx: Int, org: [Int], output: inout [[Int]] ) {
        
        if idx >= org.count {
            output.append(input)
            return
        }
        
        // take the elment
        input.append(org[idx])
        sol(input: &input, idx: idx+1, org: org, output: &output)
        
        // don't take the element
        input.removeLast()
        sol(input: &input, idx: idx+1, org: org, output: &output)
        
    }
    
    
    
    
}