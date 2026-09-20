class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count =0
        mn=0
        l=0
        freq={}
        maxx=max(nums)
        for  i in range(len(nums)):
           
            freq[nums[i]]=freq.get(nums[i],0)+1
            while freq.get(maxx,0)>=k:
               
                freq[nums[l]]-=1
                   
                l+=1

            count+=l
        return count     
        
        # maxx=max(nums)
        # for i in range(len(nums)):
        #     maxx_count=0
        #     for j in range(i,len(nums)):
        #         sub=nums[i:j+1]
        #         if nums[j]==maxx:
        #             maxx_count+=1
        #         if maxx_count >=k:
        #             count +=1         
                
        #         # if sub.count(maxx) >=k :
        #         #     count +=1
        # return count             
        