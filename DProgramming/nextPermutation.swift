//
//  PascalTraingle.swift
//  DProgramming
//
//  Created by mongy on 25/12/2021.
//

import Foundation



func nextPermutation(nums: inout [Int]) {
    
    // 1, 3, 5 ,4 , 2
    // 1, 4, 5, 3 , 2
    // 1, 4, 2, 3 , 5
   
    
    
    var k = -1
    var l = 0
    
    
    // search for break point idx
    for i in stride(from: nums.count-1, through: 0, by: -1) {
        if  i-1 >= 0   {
            if nums[i] > nums[i-1] {
                k = i-1
                break
            }
        }

    }
    
    for j  in stride(from: nums.count-1, through: 0, by: -1) {
        l = j
        if k >= 0 {
            if nums[j] > nums[k] {
               break
            }
        }
       
    }
    
    if k >= 0 {
        swapValues(arr: &nums, left: k, right: l)
        reverse(arr: &nums, start: k+1, end: nums.count-1)
        
    } else {
        // 1 2 3 4 5
        reverse(arr: &nums)
    }
    
}

func swapValues(arr: inout [Int], left: Int, right: Int) {
    let temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
}

 
func reverse(arr: inout [Int], start: Int? = nil, end: Int? = nil) {
    var  size =  arr.count/2
    
    if let s = start, let e = end {
        size = e-s+1
    }
    
    var left = start ??  0
    var right = end ??  arr.count-1
    
    
    while (left < size) {
       let temp = arr[left]
       arr[left] = arr[right]
       arr[right] = temp
        left+=1
        right-=1
    }
}



