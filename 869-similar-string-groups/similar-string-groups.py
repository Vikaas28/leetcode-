class Solution:
    def find(self, i ,p):
        if p[i]==i:
            return i
        p[i]=self.find(p[i],p)
        return p[i]
    def union(self, x, y ,r ,p):
        xp=self.find(x,p)
        yp=self.find(y,p)
        if xp == yp:
            return False
        if r[xp]>r[yp]:
            p[yp]=xp
        elif r[xp]<r[yp]:
            p[xp]=yp
        else:
            p[xp]=yp
            r[yp]+=1
        return True     
    def similar(self, s1 ,s2):
        diff=0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff+=1
                if diff >2:
                    return False
        return True                     

    def numSimilarGroups(self, strs: List[str]) -> int:
        # p=[i for i in range(len(strs))]
        # print(p)
        p=list(range(len(strs)))
        print(p)
        r=[0]*len(strs)
        n=len(strs)
        count=n
        for i in range(n):
            for j in range(i+1 ,n):
                if self.similar(strs[i],strs[j]):
                    if self.union(i , j, r ,p):
                        count-=1
        return count
