class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(l:int,r:int)->str:
            while l>=0 and r<len(s) and s[l]==s[r]:

                
                l-=1
                r+=1
            return s[l+1:r]
        res=""    
        for i in range(len(s)):
            p1=palindrome(i,i)
            if len(p1)>len(res):
                res=p1
            p2=palindrome(i,i+1)
            if len(p2) > len(res):
                res=p2    
        return res                       