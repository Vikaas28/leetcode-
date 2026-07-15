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

    def minSwapsCouples(self, row: List[int]) -> int:
        n=len(row)
        N=n//2

        parent=[i for i in range(N)]
        rank=[0]*N
        count=N
        for i in range(0,n,2):
            copule1=row[i]//2
            copule2=row[i+1]//2
            if self.union(copule1,copule2,parent,rank):

                count-=1
        print(N)        
        return N-count      
        