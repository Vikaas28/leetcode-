class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq={}
        ws=0
        l=0
        ans=0
        for j in range(k):
            ws+=nums[j]
            freq[nums[j]]=freq.get(nums[j],0)+1
        if len(freq)==k:
            ans=ws
        for i in range(k,len(nums)):
            ws-=nums[l]
            freq[nums[l]]-=1
            if freq[nums[l]]==0:
                del freq[nums[l]]
            l+=1
            ws+=nums[i]
            freq[nums[i]]=freq.get(nums[i],0)+1
            if len(freq)==k:

                ans = max(ans ,ws)
        return ans             
