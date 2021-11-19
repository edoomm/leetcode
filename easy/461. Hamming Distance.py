class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = 0
        xb = bin(x)[2:][::-1]
        yb = bin(y)[2:][::-1]
        lenmax = len(xb) if len(xb) > len(yb) else len(yb)
        
        for i in range(lenmax):
            if i < len(xb) and i < len(yb):
                if xb[i] != yb[i]:
                    diff += 1
            else:
                if i < len(xb) and xb[i] != '0':
                    diff += 1
                if i < len(yb) and yb[i] != '0':
                    diff += 1
            
        
        return diff
