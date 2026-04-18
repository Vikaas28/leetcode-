class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        mat=matrix
        r=len(mat)
        c=len(mat[0])
        for i in range(1,r):
            for j in range(1,c):
                if mat[i][j]!=mat[i-1][j-1]:
                    return False
        return True           