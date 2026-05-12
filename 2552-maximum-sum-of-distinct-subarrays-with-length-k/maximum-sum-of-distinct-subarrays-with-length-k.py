class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l=0
        wind=0
        ans=0
        freq={}
        for i  in range(len(nums)):
            wind+=nums[i]
            freq[nums[i]]=freq.get(nums[i],0)+1

            if i -l+1>k:
                wind-=nums[l]
                freq[nums[l]]-=1
                if freq[nums[l]]==0:
                    del freq[nums[l]]

                l+=1
            if i - l + 1==k and len(freq)==k:
                ans=max(ans,wind)
        return ans            