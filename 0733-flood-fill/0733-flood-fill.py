class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        nimg = image.copy()
        icolor = image[sr][sc]
        ncolor = color
        
        rows = len(image)
        cols = len(image[0])

        def dfs(r,c):
            if not ((r >= 0 and r < rows) 
                    and (c >= 0 and c < cols)
                    and (image[r][c] == icolor) and 
                   nimg[r][c] != ncolor):
                return 
            
            nimg[r][c] = ncolor
                
            dfs(r, c-1)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r+1,c)
           
        dfs(sr,sc)
        return nimg