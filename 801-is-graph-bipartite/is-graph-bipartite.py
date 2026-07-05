class Solution:
    def bfs(self, adj, color, curr,curr_color):
        q=deque()
        q.append(curr)
        color[curr]=curr_color
        while  q:
            node=q.popleft()
            for i in adj[node]:
                if color[i]==color[node]:
                    return False
                if color[i]==-1:
                    color[i]=1-color[node]
                    q.append(i)   
        return True              

    def isBipartite(self, graph: List[List[int]]) -> bool:
        v=len(graph)
        #adj=[[] for _ in range(v)]
        color=[-1]*v
        for i in range(v):
            if color[i]==-1:
                if self.bfs(graph,color,i,0)==False:
                    return False
        return True            
                         