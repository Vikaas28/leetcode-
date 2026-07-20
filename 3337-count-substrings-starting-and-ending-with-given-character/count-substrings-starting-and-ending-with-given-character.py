class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        freq=Counter(s)
        count=0
        for key , v in freq.items():
            if key ==c :
                count+=(v*(v+1))//2
        return count        