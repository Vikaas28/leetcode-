class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        sub=0
        count=0
        for i in s:
            if i ==c:
                sub+=count+1
                count+=1
        return sub        
