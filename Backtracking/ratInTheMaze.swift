//
//  ratInTheMaze.swift
//  DProgramming
//
//  Created by mongy on 7/16/21.
//

import Foundation



func getTheRatePath(maze: inout [[Int]],
                    sol: inout [[Int]],
                    row: Int,
                    col: Int,
                    goal: Int )  {
    
    if row == maze.count-1 && col == maze.count-1  {
        sol[row][col] = 1
        return
    }
    
    // do something
    sol[row][col] = 1
    
    let postions = generateNextRatPostions(row: row, col: col)
    
    if postions.isEmpty {
        // undo
        sol[row][col] = 0
        return
    }
    
    // recursion
    for pos in postions {
        if isValidPosition(n: maze.count, row: pos.row, col: pos.col, maze: &maze) {
            getTheRatePath(maze: &maze,
                       sol: &sol,
                       row: pos.row,
                       col: pos.col,
                       goal: goal)
        }
       
    }
    
}



private func generateNextRatPostions(row: Int, col: Int) -> [(row: Int, col: Int)] {
    var postions: [(row: Int, col: Int)] = []
    
    let right = (row: row, col: col+1)
    let down = (row: row+1, col: col)
    
    postions.append(contentsOf: [right, down ])
    
    return postions
}



private func isValidPosition(n: Int, row: Int, col: Int, maze: inout [[Int]])  ->  Bool {
   return row>=0 &&  row<n &&  col>=0 &&  col<n &&  (maze[row][col] == 1)
}

