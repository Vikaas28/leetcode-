class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        r=len(matrix)
        c=len(matrix[0])
        hash_map={}
        for i in range(r):
            for j in range(c):
                if i-j  in  hash_map and hash_map[i-j]!=matrix[i][j]:
                    return False
                hash_map[i-j]=matrix[i][j]    
        return True             