class Solution:
    def dfs(self, u, v, adj,st):
        v[u]=True
        count=1
        for i in adj[u]:
            if not v[i]:
                count+=self.dfs(i,v,adj,st)
                    

                    
        st.append(u)
        return count
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for  _ in range(n)]
        visited=[False]*n
        for u ,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        count=0 
        res=[] 
        sizes=[]
        total=(n*(n-1))//2
        reach=0



        for i in range(n):
            if visited[i]:
                continue
            res=[]    

            size=self.dfs(i,visited,adj,res)
            sizes.append(size)
            

        for i in sizes:
            reach+=(i*(i-1))//2


            #size=len(res)
            print(i)
            


                    
        return (total-reach)         


        