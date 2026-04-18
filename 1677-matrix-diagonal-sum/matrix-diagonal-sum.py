class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ=0
        n=len(mat)
        mid=n//2
        for i in range(n):
            summ+=mat[i][i] + mat[n-1-i][i]
        if n%2 ==1:
            summ-= mat[mid][mid]
        return summ    