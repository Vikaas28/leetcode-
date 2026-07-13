class Solution:

    def find(self,i,p):
        if p[i]==i:
            return i 
        p[i]=self.find(p[i],p)
        return p[i]
    def union(self, x,y,p,r):
        x_p=self.find(x,p)
        y_p=self.find(y,p)
        if x_p==y_p:
            return False
        if r[x_p]>r[y_p]:
            p[y_p]=x_p
        elif r[x_p]<r[y_p]:
            p[x_p]=y_p
        else:
            p[x_p]=y_p
            r[y_p]+=1
        return True                
    def equationsPossible(self, equations: List[str]) -> bool:


        parent = [i for i in range(26)]

        rank=[0]*26
        for s in equations:
            if s[1]=='=' : 
                first = ord(s[0]) - ord('a')
                second = ord(s[3]) - ord('a')
                self.union(first,second,parent,rank)

        for s in equations:
            if s[1]=='!':
                first = ord(s[0]) - ord('a')
                second = ord(s[3]) - ord('a')

                f_p = self.find(first, parent)
                s_p = self.find(second, parent)
                if f_p==s_p:
                    return False
        return True             