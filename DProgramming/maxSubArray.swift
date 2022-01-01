//
//  maxSubArray.swift
//  DProgramming
//
//  Created by mongy on 27/12/2021.
//

import Foundation


func maxSubArray(_ nums: [Int]) -> Int {
      
    
    
    var sum = 0
    var maxSum = nums[0]
    
    for num in nums {
        sum += num
        maxSum = max(sum, maxSum)
        if sum < 0 {
            sum = 0 
        }
    }
    
    return maxSum
    
  }




