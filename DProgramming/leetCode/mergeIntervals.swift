//
//  mergeIntervals.swift
//  DProgramming
//
//  Created by mongy on 01/01/2022.
//

import Foundation


// [ [1,3], [2,6], [8,10], [15,18] ]
// [[2,3],[4,5],[6,7],[8,9],[1,10]]

//  [15,18]

func merge(_ intervals: [[Int]]) -> [[Int]] {
    
    
    var intervals = intervals
    intervals.sort { ($0[0]) < ($1[0]) }

    
    var tempPair: [Int] = intervals.first ?? []
    
    var result: [[Int]] = []
    
    
    for i in 1..<intervals.count {
        
        if isOverlaping(left: tempPair, right: intervals[i]) {
           let mergedPair = mergePairs(left: tempPair, right: intervals[i])
           tempPair = mergedPair
        } else {
            result.append(tempPair)
            tempPair =  intervals[i]
        }
    }
    
    result.append(tempPair)
    
    return result
}

func isOverlaping(left: [Int], right: [Int]) -> Bool {
    right.first! < left.last!
}

func mergePairs(left: [Int], right: [Int]) -> [Int] {
    return  [min(left.first!, right.first!), max(left.last!, right.last!)]
}
