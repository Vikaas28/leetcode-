class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        from collections import deque

        #bfs  attack on titan annology same 
        #Values can create cycles → need visited tracking
        #bfs/dfs recongnition Keywords: jump, reach, can reach, any index, start position
        q=deque([start])
        n=len(arr)
        visited=set()
        while q:
            i=q.popleft()
            if i < 0 or i >= n or i in visited:
                 continue
            if arr[i]==0:
                return True
            visited.add(i)
            q.append(i+arr[i])
            q.append(i-arr[i])
        return False