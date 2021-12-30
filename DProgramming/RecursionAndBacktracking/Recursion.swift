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


