class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        freq={}
        count =0
        l=0
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
          
        #for key , val in freq.items():
            while len(set(nums))==len(freq.keys()):
                
                #l+=1
                count+=len(nums)-i
                freq[nums[l]]-=1
                if freq[nums[l]]==0:
                    del freq[nums[l]]
                
                l+=1
        print(len(freq.keys()))          
        return count         
