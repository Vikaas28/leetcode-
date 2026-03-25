class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        row=len(grid)
        col=len(grid[0])
        visited=set()

        def dfs(r,c):
            if r<0 or c < 0 or r>=row  or c>=col or grid[r][c]==0 or (r, c) in visited :
                return 0
            visited.add((r,c))


            
            res=1
            grid[r][c]=0

            res+=dfs(r+1,c)
            res+=dfs(r-1,c)
            res+=dfs(r,c+1)
            res+=dfs(r,c-1)
            return res 
        maxx=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and (i,j) not in visited:
                    maxx=max(maxx,dfs(i,j))
        return maxx                    