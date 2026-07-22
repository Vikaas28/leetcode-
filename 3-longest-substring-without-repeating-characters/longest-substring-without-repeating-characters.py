class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        l=0  #slow pointer 
        res=0
        
        for r in range(len(s)):  #fast pointer 
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            res=max(res,r-l+1)
        return res        