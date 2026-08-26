class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        lenn=0
        ans=""
        
        for i in range(len(s)):
            for j in range(i ,len(s)):
                sub=s[i:j+1]
                lenn=i-j+1
                if sub.count("1")==k:
                    if  not ans or len(sub)<len(ans) or len(sub) ==len(ans) and sub < ans :
                        ans=sub

        return ans 