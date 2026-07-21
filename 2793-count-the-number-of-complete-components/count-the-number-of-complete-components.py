class Solution:

    def dfs(self, u, v, adj,p):
        v[u]=True
        for i in adj[u]:
            if not v[i]:
                self.dfs(i, v, adj ,p)
        p.append(u)

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for _ in range(n)]
        for u ,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        count=0
        p=[]
        visited=[False]*n
        for i in range(n):
            if  visited[i]:
                continue
            res=[]    
            self.dfs(i, visited,adj,res)    
            v=len(res)
            total_sum=sum(len(adj[i]) for i in res)
            if total_sum//2 ==v*(v-1)//2:
                count+=1
        return count        



           
        