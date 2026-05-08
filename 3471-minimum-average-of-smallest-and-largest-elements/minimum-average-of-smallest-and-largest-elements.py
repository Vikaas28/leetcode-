class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avg=0
        ans=float('inf')
        nums.sort()
        l=0
        r=len(nums)-1
        while l<=r:
            avg=(nums[l]+nums[r])/2
            ans=min(ans,avg)
            l+=1
            r-=1
        return ans 