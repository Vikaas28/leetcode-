class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        for index, value in enumerate(s):
            if freq[value]==1:
                return index
        return -1            