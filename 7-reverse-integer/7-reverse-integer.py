class Solution:
    def reverse(self, x: int) -> int:
        low =  -2 ** 31
        high =  2 ** 31 - 1
        xstr = str(x)
        xlen = len(xstr)        
        
        res = ""
        for i in range(xlen-1, -1, -1):
            if xstr[i] != "-":
                res += xstr[i]
        if xstr[0] == "-":
            res = "-" + res
        
        intnum = int(res)
        
        if intnum > high or intnum < low:
            return 0 
        
        return intnum     