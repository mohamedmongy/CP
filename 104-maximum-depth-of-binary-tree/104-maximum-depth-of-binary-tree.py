# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
             return 0 
            
            
        return self.bfs(root)   
         # return 1 + max(self.dfs(root.left), self.dfs(root.right))
        
        
    def bfs(self, root: TreeNode) -> int :
            res = 0 
            q =  deque( [root])
            
            while q:
                for i in range(len(q)):
                        node = q.popleft() 
                        if node.left: 
                            q.append( node.left)
                        if node.right: 
                            q.append( node.right)

                res += 1   
            return res 
                        
    
    
    
    
      #def dfs(self, node: TreeNode):
       # if not node: 
        #    return 0 
        
        #left = self.dfs(node.left)
        #right = self.dfs( node.right)
        
        #return  1 + max(left, right)
    
    
    
        
       
        
 
            
  
        
       
        