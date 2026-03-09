
from collections import Counter 
class Solution:
    def frequencySort(self, s: str) -> str:
        #s=list(s)
        #bucket sort
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        buc=[[]for _ in range(len(s)+1)]    
        for char , f in freq.items():
            buc[f].append(char)
        res=[]
        for j in range(len(buc)-1,0,-1):
            for char in buc[j]:
                res.append(char*j)

        return "".join(res)                