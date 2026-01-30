class Solution:
    import math 
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        leftsum=[0] * n
        rightsum=[0] * n
        new =[0] * n
        for i in range(1,n):
            leftsum[i]=leftsum[i-1]+nums[i-1]
        for j in range(n-2,-1,-1) :
            rightsum[j]=rightsum[j+1]+nums[j+1]  
        for k in range(n):
            new[k]=abs(leftsum[k]-rightsum[k])
        return new          