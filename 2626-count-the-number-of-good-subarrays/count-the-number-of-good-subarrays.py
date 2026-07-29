class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        l=0
        count=0
        mn=0
        pairs=0
        freq={}
        for i in range(len(nums)):
            pairs += freq.get(nums[i], 0)
            freq[nums[i]]=freq.get(nums[i],0)+1
            #pairs+=freq[nums[i]]
            while pairs>=k:
                count+=len(nums)-i
                freq[nums[l]]-=1
                # if freq[nums[l]]==0:
                #     del freq[nums[l]]
                pairs-=freq[nums[l]]
                l+=1
            
        return count             
