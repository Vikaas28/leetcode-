class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        ans=[]
        idd=[0]*n
        for i in range(1,n):
            if nums[i] - nums[i-1]<=maxDiff:
                idd[i]=idd[i-1]
            else:
                idd[i]=i
        for u,v in queries:
            if idd[u]==idd[v]:
                ans.append(True)
            else:
                ans.append(False)
        return ans                        