
import Foundation



public func generateParenthesis(ans: inout [String], open: Int, closed: Int, max: Int, currentStr: inout String) {
    
    if currentStr.count == max*2 {
        ans.append(currentStr)
    }
    
    if open < max {
        // Do Something
        currentStr.append("(")
        // Recursion
        generateParenthesis(ans: &ans, open: open+1, closed: closed, max: max, currentStr: &currentStr)
        // Backtrack to the previous step and undo required work
        currentStr.removeLast()
    }
    
    if closed < open {
        currentStr.append(")")
        generateParenthesis(ans: &ans, open: open, closed: closed+1, max: max, currentStr: &currentStr)
        currentStr.removeLast()
    }
    
}
