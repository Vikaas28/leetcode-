class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        mydist=abs(target[0])+abs(target[1])
        for ghost in ghosts:
            ghost=abs(ghost[0]-target[0])+ abs(ghost[1]-target[1])
            if ghost<= mydist:
                return False
        return True         