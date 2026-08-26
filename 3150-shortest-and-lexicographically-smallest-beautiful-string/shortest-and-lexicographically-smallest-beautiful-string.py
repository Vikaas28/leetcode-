class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # lenn=0
        # ans=""
        
        # for i in range(len(s)):
        #     for j in range(i ,len(s)):
        #         sub=s[i:j+1]
        #         lenn=i-j+1
        #         if sub.count("1")==k:
        #             if  not ans or len(sub)<len(ans) or len(sub) ==len(ans) and sub < ans :
        #                 ans=sub

        # reurn ans 
        l=0
        count=0
        mn=""
        for  i in range(len(s)):
            if s[i]=="1":
                count+=1


            while count==k:
                sub=s[l:i+1]
                if not mn or len(sub)<len(mn) or len(sub)==len(mn) and sub < mn:
                    mn=sub
                if s[l]=="1" :
                    count-=1
                l+=1
        return mn            
