class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n=len(nums)
        total=sum(nums)
        l=0
        for i,e in enumerate(nums):
            r=total-l-e
            if l==r:
                return i
            l+=e
        return -1        
