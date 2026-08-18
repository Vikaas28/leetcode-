class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:

        # freq={}
        # ans=-1
        # l=0
        # for i in range(len(nums)):
        #     freq[nums[i]]=freq.get(nums[i],0)+1
        #     if freq[nums[i]]>=1:
        #         freq[nums[i]]-=1
        #         nums[l]-=1
        #     l+=1
        #     ans=i-l+1
        # return ans    

        ans =-1
        freq={}
        for i in range(len(nums)-k+1):
            seen=set(nums[i:i+k])
            for num in seen:
                freq[num]=freq.get(num,0)+1
        for key ,val in freq.items():
            if val==1:
                ans=max(ans,key)
        return ans                 


        