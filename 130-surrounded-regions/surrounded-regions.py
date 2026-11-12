class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        visited=set()

        def dfs(r,c):

            if r<0 or c <0 or r>=m or c>=n or (r,c) in visited or board[r][c]!='O':
                return 
            visited.add((r,c))    

            board[r][c]="T"
            dir=[(1,0),(0,1),(-1,0),(0,-1)]
            #visited.add((r,c))
            for dr , dc in dir:
                dfs(r+dr,c+dc)
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n - 1] == 'O':
                dfs(i, n - 1)
                
        # 2. Traverse first and last rows
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[m - 1][j] == 'O':
                dfs(m - 1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    #dfs(i,j)
                    board[i][j]="X"
                elif board[i][j]=="T":
                    board[i][j]="O"

        