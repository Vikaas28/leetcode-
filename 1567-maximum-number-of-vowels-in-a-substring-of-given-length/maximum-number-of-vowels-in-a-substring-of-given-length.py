class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        # vowels=set("aeiou")
        # maxx=0
        # for i in range(len(s)-k+1):
            
        #     sub=s[i:i+k]
        #     count=0
        #     for v in sub:
        #         if v in vowels:
        #             count+=1
        #     maxx=max(maxx,count)
        # return maxx                
        vowels=set("aeiou")
        ws=sum(1 for i in range(k) if s[i] in vowels)
        ans=ws
        for i in range(k,len(s)):
            if s[i] in vowels:
                ws+=1
            if s[i-k] in vowels:
                ws-=1
            ans=max(ans ,ws)
            if ans ==k:
                return k
        return ans             