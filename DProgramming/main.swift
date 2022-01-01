//
//  main.swift
//  DProgramming
//
//  Created by mongy on 7/16/21.
//

import Foundation


// coding interview question Series
//var matrix = [ [5,1,9,11],
//               [2,4,8,10],
//               [13,3,6,7],[15,14,12,16]]
//rotateMatrix(&matrix)
//print(matrix)

print(sumToMax(i: 0, max: 3))


//printNameFive(count: 0, max: 6)
//print(maxProfit([7,1,5,3,6,4]))

//var arr = [2,0,2,1,1,0]
//sortColors(&arr)
//print(arr)

//print(maxSubArray([-1,2,3]))

//var arr = [1,3,2]
//nextPermutation(nums: &arr)
////var arr = [1,2,3,4,5]
////reverse(arr: &arr)
//print(arr)


//let traingle =  generate(5)
//
//for i in traingle {
//    print(i)
//}


//print(getLongestSubStringWithOutRepeating(str: "pwwkew"))


//fizzBuzz(x: 15)

///////////////////////////////////////////                 Biary tree Problem


//let minVal = Int.min
//
//let count = goodnodesCount(node: 1, minVal: minVal)
//print(" Good Node Count \(count)")
//


    ///////////////////////////////////////////                 BackTracking Problem


    /// knight Tour combination
//private var knightSol = [   [0,-1,-1,-1,-1,-1,-1,-1],
//                            [-1,-1,-1,-1,-1,-1,-1,-1],
//                            [-1,-1,-1,-1,-1,-1,-1,-1],
//                            [-1,-1,-1,-1,-1,-1,-1,-1],
//                            [-1,-1,-1,-1,-1,-1,-1,-1],
//                            [-1,-1,-1,-1,-1,-1,-1,-1],
//                            [-1,-1,-1,-1,-1,-1,-1,-1],
//                            [-1,-1,-1,-1,-1,-1,-1,-1]
//                         ]
//
//if solveKT(row: 0, col: 0, movesCount: 1, sol: &knightSol) {
//    for i in knightSol {
//       print(i, separator: ",", terminator: "\n")
//    }
//} else {
//    print("no solution exist")
//}
   /// phone combination

//phoneCombinations(digits: [2,3,4])

  ///  NQueen
//
//private var queenBoard = [ [0,0,0,0],
//                           [0,0,0,0],
//                           [0,0,0,0],
//                           [0,0,0,0]
//                        ]
//
//var queens  = 4
//var col = 0
//
//
//var nQueens: Int = 4
//
//if getQueensPath(board: &queenBoard, nQueens: &queens, col: col) {
//    for arr in queenBoard {
//        print(arr, separator: ",", terminator: "\n")
//    }
//}

    
/// ratInTheMaze

//private var maze = [ [1,1,0,0],
//                     [0,1,0,0],
//                     [0,1,1,0],
//                     [0,0,1,1]
//                  ]
//
//var ratSolPath = [ [0,0,0,0],
//                   [0,0,0,0],
//                   [0,0,0,0],
//                   [0,0,0,0]
//                 ]
//
////                   [1,0,0,0],
////                   [1,1,0,0],
////                   [0,1,1,0],
////                   [0,0,1,1]
//
//getTheRatePath(maze: &maze, sol: &ratSolPath, row: 0, col: 0, goal: maze.count-1)
//for i in ratSolPath {
//    print(i, separator: " ", terminator: "\n")
//}

  ///  wordSearch
//var word = ""
//var arr =   [  ["a","g","c","e"],
//               ["s","f","c","s"],
//               ["a","d","e","e"],
//               ["a","d","e","e"]
//            ]
//
//
//var visietdPostion =  [
//                        [false,false,false,false],
//                        [false,false,false,false],
//                        [false,false,false,false],
//                        [false,false,false,false]
//                     ]
//
//if wordSearch(visitedArr: &visietdPostion, arr: &arr, word: &word, row: 0, col: 0, wordToSearch: "agccedda") {
//    print(" congrat!!! word found")
//} else {
//    print("opps!!! word not found")
//}

///  Generate Parenthesis
//var ans: [String] = []
//let max = 3
//var currentStr: String = ""
//generateParenthesis(ans: &ans, open: 0, closed: 0, max: 3, currentStr: &currentStr)
//print(ans)






























































































        ///////////////////////////////////////////                 Binary tree Problem


///             Is valid binary search tree

//isBinarySearchTree(root: <#T##Int#>)

///                tree right view


//var rightViewRes: [Int] = []
//var reachedLvl = 0
//rightView(root: 1, currentLvl: 1, reachedLvl: &reachedLvl, rightViewRes: &rightViewRes)
//print( "the right view is: \(rightViewRes)" )


///                 good node  path
//let minVal = Int.min
//let count = goodnodesCount(node: 1, minVal: minVal)
//print(" Good Node Count \(count)")
//




            ///////////////////////////////////////////                 BackTracking Problem



            /// knight Tour combination

//private var knightSol = [   [0,-1,-1,-1,-1,-1,-1,-1],
//                            [-1,-1,-1,-1,-1,-1,-1,-1],
//                            [-1,-1,-1,-1,-1,-1,-1,-1],
//                            [-1,-1,-1,-1,-1,-1,-1,-1],
//                            [-1,-1,-1,-1,-1,-1,-1,-1],
//                            [-1,-1,-1,-1,-1,-1,-1,-1],
//                            [-1,-1,-1,-1,-1,-1,-1,-1],
//                            [-1,-1,-1,-1,-1,-1,-1,-1]
//                         ]
//
//if solveKT(row: 0, col: 0, movesCount: 1, sol: &knightSol) {
//    for i in knightSol {
//       print(i, separator: ",", terminator: "\n")
//    }
//} else {
//    print("no solution exist")
//}

           /// phone combination

   
//phoneCombinations(digits: [2,3,4])


          ///  NQueen

//
//private var queenBoard = [ [0,0,0,0],
//                           [0,0,0,0],
//                           [0,0,0,0],
//                           [0,0,0,0]
//                        ]
//
//var queens  = 4
//var col = 0
//
//
//var nQueens: Int = 4
//
//if getQueensPath(board: &queenBoard, nQueens: &queens, col: col) {
//    for arr in queenBoard {
//        print(arr, separator: ",", terminator: "\n")
//    }
//}


            
        /// ratInTheMaze


//private var maze = [ [1,1,0,0],
//                     [0,1,0,0],
//                     [0,1,1,0],
//                     [0,0,1,1]
//                  ]
//
//var ratSolPath = [ [0,0,0,0],
//                   [0,0,0,0],
//                   [0,0,0,0],
//                   [0,0,0,0]
//                 ]
//
////                   [1,0,0,0],
////                   [1,1,0,0],
////                   [0,1,1,0],
////                   [0,0,1,1]
//
//getTheRatePath(maze: &maze, sol: &ratSolPath, row: 0, col: 0, goal: maze.count-1)
//for i in ratSolPath {
//    print(i, separator: " ", terminator: "\n")
//}


          ///  wordSearch

//var word = ""
//var arr =   [  ["a","g","c","e"],
//               ["s","f","c","s"],
//               ["a","d","e","e"],
//               ["a","d","e","e"]
//            ]
//
//
//var visietdPostion =  [
//                        [false,false,false,false],
//                        [false,false,false,false],
//                        [false,false,false,false],
//                        [false,false,false,false]
//                     ]
//
//if wordSearch(visitedArr: &visietdPostion, arr: &arr, word: &word, row: 0, col: 0, wordToSearch: "agccedda") {
//    print(" congrat!!! word found")
//} else {
//    print("opps!!! word not found")
//}


        ///  Generate Parenthesis

//var ans: [String] = []
//let max = 3
//var currentStr: String = ""
//generateParenthesis(ans: &ans, open: 0, closed: 0, max: 3, currentStr: &currentStr)
//print(ans)


//
//var numbers = [11, 59, 3, 2, 53, 17, 31, 7, 19, 67, 47, 13, 37, 61, 29, 43, 5, 41, 23]
//numbers = numbers.sorted()
//
//func linearSearch<T: Equatable>(_ a: [T], _ key: T) -> Int? {
//    for i in 0..<a.count {
//        if a[i] == key {
//            return i
//        }
//    }
//    return nil
//}
//
////print(linearSearch(numbers, 3))
//
//
//func bsearch(arr: [Int], key: Int) -> String {
//
//    let center = arr.count/2
//
//    if arr.isEmpty {
//        return "key not found "
//    }
//
//    if key == arr[center] {
//        return "key found"
//    }
//
//    if key > arr[center] {
//        let subarr = arr[center+1..<arr.count]
//        return bsearch(arr:  Array(subarr), key: key)
//    }
//
//
//    if key < arr[center] {
//        let subarr = arr[0..<center]
//       return bsearch(arr:  Array(subarr), key: key)
//    }
//
//
//    return "key not found"
//
//}
//
////print(bsearch(arr: numbers, key: 23))
////print(bsearch(arr: numbers, key: 1000))
////print(bsearch(arr: numbers, key: 67))
//
//
//print(" ------------------------------------------------------ ")
//
//
//func iterativeBsearch(arr: [Int], key: Int) -> String {
//
//    // indices
//    var low = 0
//    var high = arr.count
//
//
//    while low < high {
//
//        let center = low + (high-low)/2
//
//        if key == arr[center] {
//            return "key found"
//        }
//
//        if key > arr[center] {
//           low = center+1
//        } else {
//            high = center
//        }
//
//    }
//
//    return "key not found"
//
//}
//
//
////print(iterativeBsearch(arr: numbers, key: 23))
//print(iterativeBsearch(arr: numbers, key: 1000))
////print(iterativeBsearch(arr: numbers, key: 67))


//print(" ---------------------- Quick Sort -------------------------------- ")

// quick sort: it depend on chossing the perfect
// sort is not happen in place

//var list = [ 10, 0, 3, 9, 2, 14, 27]

//func quiukSort(arr: [Int]) -> [Int] {
//
//    if arr.count < 1 {
//        return arr
//    }
//
//    let idx = arr.count/2
//    let pivot = arr[idx]
//
//    let less = arr.filter { $0 < pivot }
//    let equal = arr.filter { $0 == pivot }
//    let greater = arr.filter{ $0 > pivot }
//
//    return quiukSort(arr: less) + equal + quiukSort(arr: greater)
//}
//
//print(quiukSort(arr: list))

//
//func partiotionInPlace(arr: inout [Int], low: Int, high: Int) -> Int {
//
//    var i = low
//    let pivot = arr[high]
//
//    for j in low..<high {
//        if arr[j] <= pivot {
//            arr.swapAt(i, j)
//            i+=1
//        }
//    }
//
//    arr.swapAt(i, high)
//
//    return i
//}
//
//
//func inPlaceQuiukSort(arr: inout [Int], low: Int, high: Int)  {
//    if low < high {
//        let pivotIdx = partiotionInPlace(arr: &arr, low: low, high: high)
//        inPlaceQuiukSort(arr: &arr, low: low, high: pivotIdx-1)
//        inPlaceQuiukSort(arr: &arr, low: pivotIdx+1, high: high)
//    }
//}
//
//
//inPlaceQuiukSort(arr: &list, low: 0, high: list.count-1)
//print(list)
//



