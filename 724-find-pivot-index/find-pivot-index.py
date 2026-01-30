class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        total=sum(nums)
        left =0
        for i , e in enumerate(nums):
            right=total-left-e
            if left ==right :
                return i 
            left +=e
        return -1        