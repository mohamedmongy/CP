class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        
        
        var map: [String: [String]] = [ : ]
           
           for str in strs {
           
               // eat >> aet
               let sortedstr = String(str.sorted())
               
               // update the key f
               if map[sortedstr] == nil {
                  map[sortedstr] = [str]
               } else  {
                   var oldvalues = map[sortedstr]!
                   oldvalues.append(str)
                   map.updateValue(oldvalues, forKey: sortedstr)
               }
           }
        
        var res: [[String]] = []
        
        let values = Array(map.values)
        
        res.append(contentsOf: values)
        
        return res
    }
}