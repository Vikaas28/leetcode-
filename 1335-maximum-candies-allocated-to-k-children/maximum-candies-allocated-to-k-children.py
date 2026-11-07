class Solution:
    def num(self, nums , able , k):
        t=0
        for i in nums:
            t+=i//able
        return t>=k

        # w=1
        # p=0
        # for i in nums:
        #     if w+i <= able:
        #         w+=i
        #     else:
        #         p+=1
        #         w=i
        # return w <=k            

    def maximumCandies(self, candies: List[int], k: int) -> int:
        l=1
        r=max(candies)
        ans=0
        while l<=r:
            mid=(l+r)//2
            if self.num(candies,mid,k):
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans             
        