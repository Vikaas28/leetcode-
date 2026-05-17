class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=[False]*len(rooms)
        def dfs(node):
            visited[node]=True
            for v in rooms[node]:
                if not visited[v]:
                    dfs(v)
        dfs(0)
        return True if len(set(visited))==1 else False