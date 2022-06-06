class Solution {
    func twoSum(_ numbers: [Int], _ target: Int) -> [Int] {
        
        var start = 0
        var end = numbers.count - 1

        var sol: [Int] = []
        
        while start < end {
            let currSum = numbers[start] + numbers[end]
            
            if currSum == target {
                sol.append(contentsOf: [start+1, end + 1 ])
                break 
            } else if currSum < target {
                start += 1
            } else {
                end -= 1
            }
        }
        
        return sol
    }
}