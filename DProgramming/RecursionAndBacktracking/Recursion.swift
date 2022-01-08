//
//  DefaultMonthCellIdentifier.swift
//  DProgramming
//
//  Created by mongy on 29/12/2021.
//

import Foundation


func printNameFive(count: Int,max: Int)  {
    if count >= max {
        return
    }
    
    print("count: \(count)")
    printNameFive(count: count+1, max: max)
}



func sumToMax(i: Int,max: Int) -> Int {
    if i == max {
        return i
    }
    
    return i + sumToMax(i: i+1, max: max)
}




