//
//  KnightTour.swift
//  DProgramming
//
//  Created by mongy on 24/07/2021.
//

import Foundation


func solveKT(row: Int, col: Int, movesCount: Int, sol: inout [[Int]]) -> Bool {
    
    if movesCount == (sol.count*sol.count)  {
        return true
    }
            
        let candidates = generateNewCandidates(row: row, col: col)
        
        for candidate in candidates {
            if isSafePostion(row: candidate.row, col: candidate.col, board: &sol)  {
                 sol[candidate.row][candidate.col] = movesCount
                  if solveKT(row: candidate.row, col: candidate.col, movesCount: movesCount+1, sol: &sol) {
                      return true
                  } else {
                      sol[candidate.row][candidate.col] = -1
                  }
            }
        }
    
    
    return false
}


private func isSafePostion(row: Int, col: Int, board: inout [[Int]]) -> Bool {
    return row>=0 && row<board.count && col>=0 && col<board[0].count && board[row][col] == -1
}


private func generateNewCandidates(row: Int, col: Int) -> [(row: Int, col: Int)] {
    var postions: [(row: Int, col: Int)] = []
    
    let xMove = [2, 1, -1, -2, -2, -1, 1, 2]
    let yMove = [1, 2, 2, 1, -1, -2, -2, -1]
    
    for i in 0..<xMove.count {
        let nextRow = row + xMove[i];
        let nextCol = col + yMove[i];
        let nextMove = (row: nextRow, col: nextCol)
        postions.append(nextMove)
    }
    
    return postions
}
