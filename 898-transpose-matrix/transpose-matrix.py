class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r=len(matrix)
        c=len(matrix[0])

        reverse=[[0]* r for _ in range(c)]
        for i in range(r):
            for j in range(c):
                reverse[j][i]=matrix[i][j]
        return reverse        