class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non =0 
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[non]=nums[i]
                non+=1
        for i in range(non , len(nums)):
            nums[i]=0
        return nums             