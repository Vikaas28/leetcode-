class Solution:
    def minimumMoves(self, s: str) -> int:
        mp={'X':0}
        count=0

        i=0
        while i <len(s):

            if s[i] in mp:
                count+=1
                i+=3
            else:
                i+=1    

                #i=mp[i]
        return count                 
        