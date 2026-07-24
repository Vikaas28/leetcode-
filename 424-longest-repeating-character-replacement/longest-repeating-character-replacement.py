class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        mn=0
        freq={}
        maxx=0
        for i in range(len(s)):
            freq[s[i]]=freq.get(s[i],0)+1
        # goal len(sub)-max(frq)
            maxx=max(freq.values())
            while((i-l+1) - maxx )>k :
                #invalid condition 
                freq[s[l]]-=1
                l+=1
            mn=max(mn, i-l+1)
        return mn         

