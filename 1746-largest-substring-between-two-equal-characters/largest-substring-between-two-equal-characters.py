class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans=-1
        for i in range(len(s)):
            for r in range(i+1,len(s)):
                if s[i]==s[r]:
                    ans=max(ans,r-i-1)
        return ans             