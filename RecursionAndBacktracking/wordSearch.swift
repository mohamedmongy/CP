import Foundation


public func wordSearch(visitedArr: inout [[Bool]] ,arr: inout [[String]], word: inout String, row: Int, col: Int, wordToSearch: String) -> Bool {
   
    if word == wordToSearch {
        return true
    }
    
     word.append(arr[row][col])
     visitedArr[row][col] = true
     
    let postions = generateCandidatePostions(row: row, col: col)
    
    if postions.isEmpty {
        word.removeLast()
        visitedArr[row][col] = false
        return false
    } else {
        
        var res = false
        
        for pos in generateCandidatePostions(row: row, col: col) {
            if isValidPosition(n: arr.count, row: pos.row, col: pos.col, visited: &visitedArr) {
                res = wordSearch(visitedArr: &visitedArr, arr: &arr, word: &word, row: pos.row, col: pos.col, wordToSearch: wordToSearch)
                if res {
                    break
                }
            }
        }
        
       word.removeLast()
       visitedArr[row][col] = false
       return res
    }
    
}

private func generateCandidatePostions(row: Int, col: Int) -> [(row: Int, col: Int)] {
    var postions: [(row: Int, col: Int)] = []
    
    let left = (row: row, col: col-1)
    let right = (row: row, col: col+1)
    let up = (row: row-1, col: col)
    let down = (row: row+1, col: col)
    
    postions.append(contentsOf: [right, left, up, down ])
    
    return postions
}



private func isValidPosition(n: Int, row: Int, col: Int, visited: inout [[Bool]])  ->  Bool {
   return row>=0 &&  row<n &&  col>=0 &&  col<n &&  (visited[row][col] == false)
}
