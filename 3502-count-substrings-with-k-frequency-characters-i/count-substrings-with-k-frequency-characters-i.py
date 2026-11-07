class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        def most(k):
            if k < 0 :
                return 0
            mp={}
            l=0
            count=0
            for i in range(len(s)):
                mp[s[i]]=mp.get(s[i],0)+1
                while any(val >=k for val in mp.values()):
                    count+=len(s)-i
                    mp[s[l]]-=1
                    if mp[s[l]]==0:
                        del mp[s[l]]
                    l+=1
                
            return count
        ans=most(k)
        return ans      
        #return most(k)-most(k-1)                  
        