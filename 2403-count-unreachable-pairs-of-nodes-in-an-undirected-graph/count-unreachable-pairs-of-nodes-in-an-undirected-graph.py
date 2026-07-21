class Solution:
    def dfs(self, u, v, adj,st):
        v[u]=True
        for i in adj[u]:
            if not v[i]:
                self.dfs(i,v,adj,st)
                    

                    
        st.append(u)
        
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for  _ in range(n)]
        visited=[False]*n
        for u ,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        count=0 
        res=[] 


        for i in range(n):
            if visited[i]:
                continue
            res=[]    

            self.dfs(i,visited,adj,res)

            size=len(res)
            print(size)
            count+=size*(n-size)
            n-=size


                    
        return count            


        