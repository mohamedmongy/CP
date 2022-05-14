
class KthLargest {

   var k: Int
   var nums: [Int] = []
    
    init(_ k: Int, _ nums: [Int]) {
        self.k = k
        self.nums = nums
        self.nums.sort()
        //  4 8  9
        while self.nums.count > k {
            self.nums.removeFirst()
        }
    }
    
    func add(_ val: Int) -> Int {
        self.nums.append(val)
        self.nums.sort()
        
        if self.nums.count > k {
            self.nums.removeFirst()
        }
        
        return self.nums.first ?? Int.min
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * let obj = KthLargest(k, nums)
 * let ret_1: Int = obj.add(val)
 */