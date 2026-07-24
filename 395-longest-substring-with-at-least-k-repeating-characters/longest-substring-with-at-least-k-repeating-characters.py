class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        l=0
        mn=0
        n=len(s)
        freq={}
        for r in range(len(s)):
            freq[s[r]]=freq.get(s[r],0)+1
            #print(freq[s[r]])
        while l < n and freq[s[l]]>=k:
            l+=1
        if l>n -1:
            return l
        print(s[l:])    
        ls1=self.longestSubstring(s[0:l],k)
        while l <n and freq[s[l]]<k:
            l+=1
        ls2=self.longestSubstring(s[l:],k) 
        return max(ls1,ls2)    

            