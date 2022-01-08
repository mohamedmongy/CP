//
//  TreeLeftView.swift
//  DProgramming
//
//  Created by mongy on 02/08/2021.
//

import Foundation



let rightTree: [Int: (l: Int?, r: Int?) ] =
                    [
                        1: (l: 2 , r: 3),
                        2: (l: 4 , r: 5),
                        3: (l: 6,r: nil),
                        4: (l: nil ,r: 7),
                        5: (l: nil,r: nil),
                        6: (l: nil,r: nil),
                        7: (l: nil,r: nil)
                    ]

func rightView(root: Int?, currentLvl: Int, reachedLvl: inout Int,  rightViewRes: inout [Int]) {
    
    if root == nil {
        return
    }
    
    if currentLvl > reachedLvl {
        reachedLvl+=1
        rightViewRes.append(root!)
    }
    
    if let rightKid = rightTree[root!]!.r {
        rightView(root: rightKid, currentLvl: currentLvl+1, reachedLvl: &reachedLvl, rightViewRes: &rightViewRes)
    }
    
    
    if let leftKid = rightTree[root!]!.l {
        rightView(root: leftKid, currentLvl: currentLvl+1, reachedLvl: &reachedLvl, rightViewRes: &rightViewRes)
    }
    
}
