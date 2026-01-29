class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summ=sum(nums)
        n=len(nums)
        exp=n*(n+1)//2
        return exp-summ

        
        