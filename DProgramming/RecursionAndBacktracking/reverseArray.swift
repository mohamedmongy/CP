//
//  reverseArray.swift
//  DProgramming
//
//  Created by mongy on 08/01/2022.
//

import Foundation


func reverseArr(arr: [Int],reversedArr: inout [Int] , i: Int)  -> [Int] {
    
    let count = arr.count
    if i == count {
        return reversedArr
    }
    
   
    var reversed = reverseArr(arr: arr, reversedArr: &reversedArr, i: i+1)
    reversed[count-1-i] = arr[i]
    return reversed
    
}



func isPali(str: String, i: Int)  -> Bool {
    
    let count = str.count
    if i >= count/2 {
        return true
    }
    
    let val = str[str.index(str.startIndex, offsetBy: i)] ==
              str[str.index(str.startIndex, offsetBy: count-i-1)]
    
    return val && isPali(str: str, i: i+1)
    
}
