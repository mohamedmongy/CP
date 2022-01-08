//
//  Array+Extension.swift
//  DProgramming
//
//  Created by mongy on 30/12/2021.
//

import Foundation

extension Array {
   mutating func swapValues(left: Int, right: Int) {
        let temp = self[left]
        self[left] = self[right]
        self[right] = temp
    }
}
