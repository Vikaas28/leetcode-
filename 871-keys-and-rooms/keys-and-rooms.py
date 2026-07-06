class Solution:
    def dfs(self,rooms,visited,u):
        visited[u]=True
        for i in rooms[u]:
            if not visited[i]:
                self.dfs(rooms,visited,i)
                    #return False
        return True            

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=[False]*len(rooms)
        self.dfs(rooms,visited,0)
        for i in range(len(rooms)):
            if not visited[i]:
                
                return False
        return True            