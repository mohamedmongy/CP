class Solution:
    
    def checkPossible(self, prevs, nexts):
        if len(nexts) != (len(prevs) +  1):
            return False 
        
        ns = 0 
        ps = 0 
        
        while ns < len(nexts):
            if  ps < len(prevs)  and nexts[ns] == prevs[ps]:
                ns += 1
                ps += 1 
            else:
                ns += 1         
        if ns == len(nexts) and ps == len(prevs):
            return True 
        return False 
        
    def longestStrChain(self, words: List[str]) -> int:
                        
        n = len(words)
        words.sort(key=len) 
        
        dp = [ 1 for i in range(n) ] 
        
        lis = 1
        
        for cidx in range(n):
            for pidx in range(cidx):
                if self.checkPossible(words[pidx], words[cidx]) and (dp[pidx] + 1) > dp[cidx]: 
                    dp[cidx] = dp[pidx] + 1
            lis = max(lis, dp[cidx])  
   
        return lis
        