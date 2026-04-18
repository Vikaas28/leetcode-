
'''mat=matrix
        r=len(mat)
        c=len(mat[0])
        for i in range(r):
            for j in range(c):
                return mat[i][j]!=0 or mat[j][i]!=0 
                '''
from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        
        for r in range(n):
            row = set()
            col = set()
            
            for c in range(n):
                
                if matrix[r][c] in row:
                    return False
                row.add(matrix[r][c])
                
                
                if matrix[c][r] in col:
                    return False
                col.add(matrix[c][r])
        
        return True        
