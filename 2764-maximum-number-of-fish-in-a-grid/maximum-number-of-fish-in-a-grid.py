class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        row =len(grid)
        col=len(grid[0])
        def dfs(r,c):
            if r <0 or r>=row or c<0 or c>= col or grid[r][c]==0:
                return 0
            res=grid[r][c]    
            grid[r][c]=0
            res+=dfs(r+1,c)
            res+=dfs(r-1,c)
            res+=dfs(r,c+1)
            res+=dfs(r,c-1)
            return res 
        maxx=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    maxx=max(maxx,dfs(i,j))
        return maxx                    