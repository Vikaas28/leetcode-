class Solution:
    def find(self,i,p):
        if p[i]==i:
            return i
        p[i]=self.find(p[i],p)
        return p[i]
    def union(self,x,y,p,r):
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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ans=n
        print(len(connections))
        if len(connections)<n-1:
            return -1
        p=[ i for i in range(n)]
        r=[0]*n
        for u , v in connections:
            
            if self.union(u,v,p,r):
                ans-=1
                
        #print(p)
        return ans-1
        