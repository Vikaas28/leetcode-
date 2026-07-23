class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # count=0
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         sub=s[i:j+1]
        #         if all(char in sub for char in s):
        #             count+=1
        # return count             
        last={'a':-1,'b':-1,'c':-1}
        count=0
        for i in range(len(s)):
            last[s[i]]=i
            #print(last)
            
            if last[s[i]]!=-1:
                mini=min(last['a'],last['b'],last['c'])
                count+=mini+1
        return count        

