class Solution:
    def dfs(self , adj, u ,destination, visited):
        if u==destination:
            return True
        visited[u]=True
        for i in adj[u]:
            if not visited[i]:
               if  self.dfs(adj,i,destination,visited):
                return True
        return False        
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj=[[] for _ in range(n)]
        for u , v  in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited=[False]*n
        #visited[source]=True
        return self.dfs(adj,source,destination,visited)
        #return visited[destination]        