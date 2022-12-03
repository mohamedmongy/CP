#User function Template for python3
from collections import deque

class Solution:
    
    def findOrder(self,dict, N, K):
        w = N
        l = K
        
        adj = [ [] for n in range(K) ]
        
        # create graph edges
        for i in range(w-1):
            s1 = dict[i]
            s2 = dict[i+1]
            mln = min(len(s1), len(s2))
            
            for j in range(mln): 
                if s1[j] != s2[j]:
                    adj[ord(s1[j]) - ord("a")].append(ord(s2[j]) - ord("a"))
                    break
        # print(adj)
        return self.topoSort(K, adj)
        
    def topoSort(self, V, adj):
        # print("staerted")
        indegress = [ 0 for _ in range(V) ]
        for v in range(V):
            for n in adj[v]: 
                indegress[n] += 1

        dq = deque()
        # starter nodes
        for v in range(V): 
            if indegress[v] == 0:
                # print(v)
                dq.append(v)
                
        res = []
        
        while dq:
            node = dq.pop()
            val = chr(node + ord("a"))
            # print(val)
            res.append(val)
            
            for nbr in adj[node]:
                indegress[nbr] -= 1 
                if indegress[nbr] == 0: 
                    dq.append(nbr)
                    
        # print(res)
        resstr = "".join(res)
        # print(resstr)
        return resstr
       



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends