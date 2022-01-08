//
//   mergeSortedArray.swift
//  DProgramming
//
//  Created by mongy on 01/01/2022.
//

import Foundation



func mergeSortedArrays(_ nums1: inout [Int], _ m: Int, _ nums2: [Int], _ n: Int) {
    
    var tempArr = nums2
    
    if !nums2.isEmpty {
        
        for i in 0..<m {
            
            if nums1[i] > tempArr[0] {
                let temp =  tempArr[0]
                tempArr[0] =  nums1[i]
                nums1[i] = temp
                tempArr.sort()
            }
            
        }
        
    
        var left = 0
        
        for j in m..<nums1.count {
            nums1[j] =  tempArr[left]
            left += 1
        }
    }
    
  
        
}
