class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        sign=0
        diff=0
        count =1
        #prefix[0]=nums[0]
        for i in range(1, len(nums)):
            diff=nums[i]-nums[i-1]
        #print(diff)  
        
        
            if diff > 0 and sign<=0:
                count +=1
                sign=1
            elif diff < 0 and sign>=0:
                count+=1
                sign=-1
        return count             
        