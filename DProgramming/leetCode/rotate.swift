//
//  rotate.swift
//  DProgramming
//
//  Created by mongy on 30/12/2021.
//

import Foundation

func rotateMatrix(_ matrix: inout [[Int]]) {
    
    // transpose each row to col
    for row in 0..<matrix.count {
        for col in  row..<matrix[row].count {
            let temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp
        }
    }
    
    // reverse each col
    
    for row in 0..<matrix.count {
        
        var left = 0
        var right = matrix[row].count-1
        
        while right > left {
            let temp = matrix[row][right]
            matrix[row][right] = matrix[row][left]
            matrix[row][left] = temp
            left += 1
            right -= 1
        }
    }
        
}

