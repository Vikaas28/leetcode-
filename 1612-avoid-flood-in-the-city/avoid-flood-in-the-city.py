
class Solution:
    def avoidFlood(self,rains:list[int])->list[int]:
        def upper_bound(nums, x):
            l=0
            r=len(nums)
            while l <r:
                mid=(l+r)//2
                if nums[mid]>x:
                    r=mid
                else:
                    l=mid+1
            return l             
        n=len(rains)
        ans=[1]*n
        freq={}
        seen=[]
        for i,lake in enumerate(rains):
            if lake==0:
                seen.append(i)
            else:
                ans[i]=-1
                if lake in freq:
                    idx=upper_bound(seen,freq[lake])
                    if idx==len(seen):
                        return []
                    day=seen[idx]
                    ans[day]=lake
                    seen.pop(idx)
                freq[lake]=i
        return ans