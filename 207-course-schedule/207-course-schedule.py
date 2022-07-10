class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # fill the dictionary 
        dic = { i: [] for i in range(numCourses) }
        
        # to detect cycle 
        visitedset  = set()
        
        # update the course prequisites 
        for crs , pre in prerequisites:
            dic[crs].append(pre)
            
            
        def dfs(crs):
            if crs in visitedset:
                return False 
            
            pres = dic[crs]
            
            if pres == []:
                return True 
            
            visitedset.add(crs)
            
            for pre in pres:
                if not dfs(pre): return False
                
            dic[crs] = []    
            visitedset.discard(crs)    
            return True    
        
        for i in range(numCourses):
            if not dfs(i): return False 
            
        return True 
        
        
        