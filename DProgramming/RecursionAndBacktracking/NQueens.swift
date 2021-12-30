//
//  NQueens.swift
//  DProgramming
//
//  Created by mongy on 17/07/2021.
//

import Foundation



func getQueensPath(board: inout [[Int]],
                   nQueens: inout Int,
                   col: Int) -> Bool {
    
    
    if col >= board.count {
        return true
    }
    
    
    for r in 0..<board.count {
        
        if isValidPosition(row: r, col: col, board: &board) {
            // DoSomething
            board[r][col] = 1
            // recursive
            if getQueensPath(board: &board, nQueens: &nQueens, col: col+1) {
                return true
            }
            
            // backtrack
            board[r][col] = 0
        }
    }
    
    return false
}


private func isValidPosition(row: Int, col: Int, board: inout [[Int]])  ->  Bool {
    
    var r = row
    var c = col

   

    // check horizontally left
    c = col
    r = row
    
    while c >= 0 {
        if board[r][c] == 1 {
            return false
        }
       c-=1
    }
    
  //   check diagonal upper left
    r = row
    c = col
    
    while r >= 0 && c >= 0 {
        if board[r][c] == 1 {
            return false
        }
        r-=1
        c-=1
    }

    // check diagonal lower left
    r = row
    c = col

    while r < board.count && c>=0 {
        if board[r][c] == 1 {
            return false
        }
        r+=1
        c-=1
    }
//
    return true
}
