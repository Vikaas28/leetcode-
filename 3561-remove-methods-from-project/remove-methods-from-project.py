class Solution:
    def dfs(self, u, v, adj , p):
        v[u]=True
        for i in adj[u]:
            if not v[i]:
                self.dfs(i,v,adj,p)
        p.append(u)

    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        visited=[False]*n
        adj=[[] for _ in range(n)]
        for u , v in invocations:
            adj[u].append(v)
            
        res=[]
        self.dfs(k,visited,adj,res)
        seen=set(res)
        for u ,v in invocations :
            if u not in seen and v in seen:
                print(n)   
                return list(range(n)) 
        #print(n)   
        print(seen)     

        return [i for i in range(n) if i not in seen]               
        