class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}
        for i in s :
            freq[i]=freq.get(i,0)+1
        for i , v in enumerate(s):
            if freq[v]==1:
                return i 
        return -1                  