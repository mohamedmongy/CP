//
//  Goognode.swift
//  DProgramming
//
//  Created by mongy on 25/07/2021.
//

import Foundation


let tree: [Int: (l: Int?, r: Int?) ] =
                    [
                        1: (l: 6 , r: 9),
                        9: (l: 8 , r: nil),
                        8: (l: nil,r: nil),
                        6: (l: 2,r: 7),
                        2: (l: nil,r: nil),
                        7: (l: nil,r: nil)
                    ]

func goodnodesCount(node: Int, minVal: Int ) -> Int {
    
    var nodeAns = 0
    var leftAns = 0
    var rightAns = 0
    var currentMin = minVal
    
    if node >= minVal {
        nodeAns += 1
        currentMin = node
    }
    
    let kids = tree[node]!
    
    if kids.l == nil {
        leftAns = 0
    } else {
       leftAns = goodnodesCount(node: kids.l!, minVal: currentMin)
    }
    
    if kids.r == nil {
        rightAns = 0
    } else {
       rightAns = goodnodesCount(node: kids.r!, minVal: currentMin)
    }
    
    return nodeAns + leftAns + rightAns
   
}
