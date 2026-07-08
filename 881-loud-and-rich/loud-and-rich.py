class Solution:
    def dfs(self, adj,u,visited,p):
            if visited[u]!=-1:
                return visited[u]
            res=u    
            for i in adj[u]:
                ans=self.dfs(adj,i,visited,p)
                if p[ans]<p[res]:
                    res=ans
            visited[u]=res
            return res        
                
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        v=len(quiet)
        adj=[[] for _ in range(v)]
        for a,b,in richer:
            adj[b].append(a)
        visited=[-1]*v
        for i in range(v):
            if visited[i]==-1:
                self.dfs(adj,i,visited,quiet) 
        return visited           
        
