class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        # freq=Counter(s)
        # count=0
        # for i in range(len(s)):
        #     maxx_count=0
        #     for j in range(i , len(s)):
        #         #sub=s[i:j+1]
        #         if s[j]==k:
        #             maxx_count+=1
        #         if maxx_count>=k:
        #             count+=1
        # return count    
        freq={}
        l=0
       
        count=0
        
       
        
        for i in range(len(s)):
            
            freq[s[i]]=freq.get(s[i],0)+1 
            
            while freq.get('0',0) > k and freq.get('1',0)>k :
                freq[s[l]]-=1
                    
                #freq[s[l]]-=1
                l+=1
            count+=i-l+1
        return count         

