class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
       mini=min(nums)
       maxx=max(nums)
       res=[]
       for i in range(mini,maxx):
           if i not in  nums:
               res.append(i)
       return res        