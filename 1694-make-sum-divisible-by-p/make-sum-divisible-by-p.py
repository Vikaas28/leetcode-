class Solution:
    
    def minSubarray(self, nums: List[int], p: int) -> int:


        mp={0:-1}
        #count=0
        prefix=0
        target=sum(nums)%p
        if target ==0:
            return 0 
        minn=len(nums)
        
        for i in range(len(nums)):
            prefix+=nums[i]
            curr=prefix%p
            
            prev=(curr-target +p)%p
            if prev in mp:
                #count+=mp.get(prev%p,0)
                minn=min(minn,i-mp[prev])
                

                
            mp[curr]=i

        return minn if minn <len(nums) else -1         
            

        #count=0
        #summ=0      
        # count=len(nums)
        # t=sum(nums)
        # rem=t%p
        # if rem==0:
        #     return 0

        # for i in range(len(nums)):
            
        #     summ=0
        #     for j in range(i,len(nums)):
        #         lenn=j-i+1
        #         summ+=nums[j]
        #         sub=nums[i:j+1]
        #         target=summ% p
        #         if target == rem:
                
        #             count=min(count,lenn)
        # return count             
    #     mp={0:1}
    #     count=0
    #     k=p
    #     l=0
    #     prefix=0
    #     for i in range(len(nums)):
    #         prefix+=nums[i]
    #         if prefix % k in mp:
    #             del nums[l]
    #             l+=1
    #             count+=mp.get(prefix%k,0)
    #         mp[prefix%k]=mp.get(prefix%k,0)+1
    #     return count 

    