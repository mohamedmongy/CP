//
//  general.swift
//  DProgramming
//
//  Created by mongy on 11/12/2021.
//

import Foundation

        //    -------------- catch the theif ----------------

// -  i    -j

func catchTheifs() -> Int {
    let arr = [ "p", "t", "p" , "t", "t" , "p" , "t"]
    let k = 1

    var maxTheifCatched = 0

    for i in 0..<arr.count {

    if arr[i] == "p" {
     
     var isalreayCatchTheif = false
     
     let rightIdx = i+1
     
     if arr[rightIdx] == "t" {
         maxTheifCatched += 1
         isalreayCatchTheif = true
     }
     
     let leftIdx = i-1
     
     if leftIdx >= 0 {
         if arr[leftIdx] == "t" {
             if !isalreayCatchTheif {
                 maxTheifCatched += 1
             }
         }
     }
     
    } else {
     continue
    }
    }
    
    return maxTheifCatched
    
}


func getLongestSubStringWithOutRepeating(str: String) ->  String {
    
    var subStr = ""
    var res = ""
    
    for currentChar  in str {
        if !subStr.contains(currentChar) {
            subStr.append(currentChar)
        } else {
            if subStr.count > res.count {
                res = subStr
            }
            subStr = ""
            subStr.append(currentChar)
        }
    }
    
    if subStr.count > res.count {
        res = subStr
    }

    
    return res
}
 


func fizzBuzz(x: Int) {
    
    for j in 0..<x  {
        
        if (j % 3 == 0 && j % 5 == 0) {
            print("fizzbuzz")
        } else if j % 3 == 0 {
            print("fizz")
        } else if j % 5 == 0 {
            print("buzz")
        } else {
            print("\(j)")
        }
    }
}
