//
//  sortColors.swift
//  DProgramming
//
//  Created by mongy on 27/12/2021.
//

import Foundation


func sortColors(_ nums: inout [Int]) {
      
      var low = 0
      var mid = low
      var high = nums.count-1
      
            
     while mid <= high {
          
         switch nums[mid]  {
           case 0 :
             nums.swapAt(low, mid)
              low += 1
              mid += 1
          
          case 1:
             mid += 1
          
          case 2:
             nums.swapAt(high, mid)
             high -= 1
         default:
             break
         }
         
      }
  }
