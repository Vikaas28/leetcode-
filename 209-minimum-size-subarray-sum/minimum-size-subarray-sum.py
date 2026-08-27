class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ=0
        mn=float('inf')
        l=0
        for r in range(len(nums)):
            summ+=nums[r]
            while summ>=target:
                mn=min(mn,r-l+1)
                summ-=nums[l]
                l+=1
        return 0 if mn == float('inf') else mn        
        