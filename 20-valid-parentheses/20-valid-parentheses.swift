class Solution {
    func isValid(_ s: String) -> Bool {
        
       var stack: [String] = []
       let open = ["(": ")" , "[": "]" , "{": "}"]
       let close = [")": "(" , "]": "[" , "}": "{"]
       
       
       for c in s {
           
            if open[String(c)] != nil {
               stack.append(String(c))
           } else {
               if !stack.isEmpty && close[String(c)] != nil {
                   let val = close[String(c)]
                   if stack.last == val {
                       stack.removeLast()
                   } else { 
                      return false 
                   }
               } else {
                   return false
               }
           }
           
       }
    
       return stack.isEmpty
    }
}