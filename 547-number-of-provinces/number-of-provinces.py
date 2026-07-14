class Solution:
    def find(self,i,p):
        if p[i]==i:
            return i
        p[i]=self.find(p[i],p)
        return p[i]
    def union(self, x,y,p,r):
        xp=self.find(x,p)
        yp=self.find(y,p)
        if xp==yp:
            return False
        if r[xp]>r[yp]:
            p[yp]=xp
        elif r[xp]<r[yp]:
            p[xp]=yp
        else:
            p[xp]=yp
            r[yp]+=1
        return True


    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj=[[] for i in range(len(isConnected))]
        parent=[ i for i in range(len(isConnected))]

        rnkk=[0]* len(isConnected)
        count=len(isConnected)
        for i in range(len(isConnected)):
            for j in range(i+1,len(isConnected)):
                if  isConnected[i][j]==1:
                    if self.union(i,j,parent,rnkk):
                        count-=1
        return count                

            

       
       
                
           

        