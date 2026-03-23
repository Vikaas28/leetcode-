class Solution:
    def applyOperations(self, nums):
        
        # Step 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        # Step 2
        non = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[non] = nums[j]
                non += 1
        
        for j in range(non, len(nums)):
            nums[j] = 0
        
        return nums