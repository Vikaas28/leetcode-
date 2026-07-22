class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq={}
        l=0
        ln=0
        for i in range(len(nums)):
            #condition 
            freq[nums[i]]=freq.get(nums[i],0)+1
            while freq[nums[i]]>k:
                freq[nums[l]]-=1 #shrink
                l+=1
            ln=max(ln,i-l+1)
        return ln    

           
        