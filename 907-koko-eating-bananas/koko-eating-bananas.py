import math 
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def pos(able , arr, h):
            piles=0
            for i in arr:
                piles+=math.ceil(i/able)
            return piles<=h    
        l=1
        r=max(piles)
        ans=r
        while l<=r:
            mid=(l+r)//2
            if pos(mid, piles , h):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans             


        