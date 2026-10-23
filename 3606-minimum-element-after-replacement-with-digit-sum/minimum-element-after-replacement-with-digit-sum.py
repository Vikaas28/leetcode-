class Solution:
    def minElement(self, nums: List[int]) -> int:
        
        res=[]
        for i in nums:
            sumi=0
            while i>0:


               sumi+=i%10
               i//=10
            
            res.append(sumi)
        mini=min(res)
        return mini    