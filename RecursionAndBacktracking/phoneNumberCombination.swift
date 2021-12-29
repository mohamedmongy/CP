//
//  phoneNumberCombination.swift
//  DProgramming
//
//  Created by mongy on 22/07/2021.
//

import Foundation

let digitsMap = [ 2: ["a", "b", "c"],
                  3: ["d", "e", "f"],
                  4: ["g", "h", "i"],
                  5: ["j", "k", "l"],
                  6: ["m", "n", "o"],
                  7: ["p", "q", "r", "s"],
                  8: ["t", "u", "v"],
                  9: ["w","x", "y", "z"]
                ]


public func phoneCombinations(digits: [Int])  {
    var ans: [String] = []
    var str = ""
    backTracK(idx: 0, digits: digits, ans: &ans, str: &str)
    print(ans)
}


private func backTracK(idx: Int, digits: [Int], ans: inout [String], str: inout String) {
    
    if digits.count == str.count {
        ans.append(str)
        return
    }
    
    let digit = digits[idx]
    let letters = digitsMap[digit] ?? []
    
    for letter in letters {
        str += "\(letter)"
        backTracK(idx: idx+1, digits: digits, ans: &ans, str: &str)
        _ = str.popLast()
    }
}
