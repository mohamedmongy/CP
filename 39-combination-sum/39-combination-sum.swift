class Solution {
   func combinationSum(_ candidates: [Int], _ target: Int) -> [[Int]] {
    
    func dfs(input: inout [Int], idx: Int, output: inout [[Int]], total: Int, target: Int ) {
        
        if total == target {
            output.append(input)
            return
        }
        
        if total > target {
            return
        }
        
        if idx >= candidates.count {
            return
        }
        
        // take the elment
        input.append(candidates[idx])
        dfs(input: &input, idx: idx, output: &output, total:  total + candidates[idx], target: target)
        
        // don't take the element - back track 
        input.removeLast()
        dfs(input: &input, idx: idx+1, output: &output, total: total, target: target)
        
    }
    
    var res: [[Int]] = []
    var input: [Int] = []
    
    dfs(input: &input, idx: 0, output: &res, total: 0, target: target)
    
    return res
}
  
}