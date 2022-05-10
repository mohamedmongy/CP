/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
    func maxDepth(_ root: TreeNode?) -> Int {
         return maxD(node: root)
    }
    
    func maxD(node: TreeNode?) -> Int {
        if node == nil {
            return 0
        }
        
        var left = 0
        var right = 0
        
        if node?.left != nil {
            left = maxD(node: node?.left)
        }
        
        if node?.right != nil {
           right = maxD(node: node?.right)
        }
        
        return  1 + max(left, right)
    }
}