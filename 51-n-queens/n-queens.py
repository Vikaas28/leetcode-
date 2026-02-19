class Solution:
    def solveNQueens(self, n: int):
        res=[]
        board=[["."]*n for _ in range(n)]  # 2d aray 
        def issafe(row, col ):
            #same level
            for i in range(n):
                if board[i][col]=='Q':
                    return False
            
            #left upper diagonal 
            i,j=row-1,col-1
            while i>=0 and j>=0:
                if board[i][j]=='Q':
                    return False
                i-=1
                j-=1
            
            i=row-1
            j=col+1
            while i>=0 and j<n:
                if board[i][j]=='Q':
                    return False
                i-=1
                j+=1
            return True 


    
        def back(path):
            if path==n:
                res.append(["".join(r) for r in board])
                return
            row =path   
            for col in range(n):
                if issafe(row,col):

                    board[row][col]="Q" # set Q 

                    back(path+1)    
                    board[row][col]="." #next time visist 
        back(0)
        return res         