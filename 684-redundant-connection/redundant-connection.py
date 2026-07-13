class Solution:
    def find(self,i,p):
        if p[i]==i:return i
        p[i]=self.find(p[i],p)
        return p[i]
    def union(self, x,y,p,rank):
        x_p=self.find(x,p)
        y_p=self.find(y,p)
        if x_p==y_p:
            return False # cycle detected in graph   1--2 1--3  Xx 2--3 Xx
            
        if rank[x_p]>rank[y_p]:
            p[y_p]=x_p
        elif rank[x_p]< rank[y_p]:
            p[x_p]=y_p
        else:
            p[x_p]=y_p
            rank[y_p]+=1
        return True    

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent=[i for i in range(len(edges)+1)] #1  based index not 0 
        
        rank=[0]*(len(edges)+1) # rank  from 1 
        for u ,v in edges:
            if self.union(u,v ,parent,rank)==False:
                return [u,v]