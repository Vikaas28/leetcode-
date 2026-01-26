
from collections import Counter 
class Solution:
    def frequencySort(self, s: str) -> str:
        #s=list(s)
        freq=Counter(s)
        return "".join(
            char * count 
            for char ,count in freq.most_common()
        )
        