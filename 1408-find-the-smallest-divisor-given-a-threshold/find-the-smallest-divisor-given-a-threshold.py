class Solution:
    def num(self,nums,div,threshold):
        total=0
        for num in nums:
            total+=(num +div-1)//div
        return total<=threshold    

                
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l=1
        r=max(nums)
        ans=r
        while l <= r:
            mid=(l+r)//2
            if self.num(nums,mid,threshold):
                r=mid-1
                ans=mid
            else:
                l=mid+1   
        return ans          


        