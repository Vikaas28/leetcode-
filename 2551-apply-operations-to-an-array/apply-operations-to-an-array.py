class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        non=0 
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[non]=nums[i]
                non+=1
        for i in range( non  , len(nums)):
            nums[i]=0
        return nums                         
