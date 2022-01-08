//
//  PascalTriangle.swift
//  DProgramming
//
//  Created by mongy on 27/12/2021.
//

import Foundation

//  Pascal's Triangle

func generate(_ numRows: Int) -> [[Int]] {
    
    var arr: [[Int]] = []
    
    for row in 0..<numRows {
        
        var temp =  [Int](repeating: 1, count: row+1)
        
        temp[0] = 1
        let last = temp.count-1
        temp[last] = 1
        
        arr.append(temp)
        
        
        if row > 1 {
            
            for col in 1..<row {
                arr[row][col] =  arr[row-1][col-1] + arr[row-1][col]
            }
        }
       
        
    }
    
    
    return arr
}
