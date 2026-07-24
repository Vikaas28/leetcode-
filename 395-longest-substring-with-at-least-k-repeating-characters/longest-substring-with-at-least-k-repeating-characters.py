class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        l=0
        mn=0
        n=len(s)
        freq={}
        #print(s.split('c'))
        for r in range(len(s)):
            freq[s[r]]=freq.get(s[r],0)+1
            #print(freq[s[r]])
        for key , val in freq.items():
            if val <k:
                return max(self.longestSubstring(sub,k) for sub in s.split(key))
        return len(s)        