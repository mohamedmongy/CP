//
//  findDuplicate.swift
//  DProgramming
//
//  Created by mongy on 01/01/2022.
//

import Foundation


//  [ 3,1,3,4,2 ]

func findDuplicate(_ nums: [Int]) -> Int {
    var slow = nums[0]
    var fast = nums[0]
    
    // first collision
    repeat {
        slow = nums[slow]
        fast = nums[nums[fast]]
    } while(slow != fast)
    
    
    fast = nums[0]
    
    // move one step for each iterator
    while (fast != slow) {
        slow = nums[slow]
        fast = nums[fast]
    }
    
    return slow
    
}
