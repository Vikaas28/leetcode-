class Solution:
    def num(self, nums, able, n):
        # p=1
        # w=0
        # for i in nums:
        #     if w+i <=able:
        #         w+=i
        #     else:
        #         p+=1
        #         w=i
        # return p <= n
        total=0
        for num in nums:
            total+=(num+able-1)//able
        return total<=n   

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        r=max(quantities)
        l=1
        ans=r
        while l<=r:
            mid=(l+r)//2
            if self.num(quantities, mid , n):
                ans=mid
                r=mid-1

               
            else:
                l=mid+1
        return ans             
        