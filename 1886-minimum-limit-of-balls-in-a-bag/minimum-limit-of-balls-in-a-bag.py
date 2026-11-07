class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        def pos( able, arr, m):
            t=0
            for num in arr:
                #t+=math.ceil(num//able)
                t+=(num-1)//able
            return t<=m
        l=1
        r=max(nums)
        ans=r
        while l <=r :
            mid=(l+r)//2
            if pos(mid, nums, maxOperations) :
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
        