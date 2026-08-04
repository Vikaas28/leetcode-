class Solution:
    def pos(self,cap,weights,days):
        need=1
        curr=0
        for i in weights:
            if curr+i >cap:
                need+=1
                curr=0
            curr+=i
        return need<=days        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l=max(weights)
        r=sum(weights)
        ans=r
        while l<=r:
            mid=(l+r)//2
            if self.pos(mid,weights,days):
                ans=mid
                r=mid-1 #first occurencw
            else:
                l=mid+1

        return ans            

        