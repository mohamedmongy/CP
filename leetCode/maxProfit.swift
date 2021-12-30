//
//  maxProfit.swift
//  DProgramming
//
//  Created by mongy on 28/12/2021.
//

import Foundation

func maxProfit(_ prices: [Int]) -> Int {
    
    let count  = prices.count
    var minimm = Int.max
    var profit = 0
   
    
    for i in 0..<count {
        minimm = min( prices[i], minimm)
        let tempProfit = prices[i] - minimm
        profit = max(profit, tempProfit)
    }
    
    return profit
}
