class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l=0
        summ=0
        count=0
        for x in range(len(nums)):
            summ+=nums[x]
            while summ *(x-l+1)>=k :
                summ-=nums[l]
                l+=1
            count+=(x-l+1)
        return count             