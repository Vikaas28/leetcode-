class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        ans=nums[0]
        while(l<=h):
            mid=(l+h)//2
            ans=min(ans,nums[mid])
            if nums[l]==nums[mid] and nums[mid] == nums[h]:
                l+=1
                h-=1
            elif nums[mid]> nums[h]:
                l=mid+1
            else:
                h=mid-1
        return ans                 