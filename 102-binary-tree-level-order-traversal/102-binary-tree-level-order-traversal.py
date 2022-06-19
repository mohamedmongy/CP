# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        if not root: 
            return []
        
        q = deque([root])
        
        while q: 
           
            length = len(q) 
            templist = []
            
            #for i in range(length): 
             #   templist.append(q[i].val)
            #res.append(templist)
                       
           
            for i in range(length): 
                tmp = q.popleft()
                templist.append(tmp.val)
                if tmp.left: 
                    q.append(tmp.left)
                if tmp.right: 
                    q.append(tmp.right)    
            res.append( templist)
        return res 
       
    
        
        
        