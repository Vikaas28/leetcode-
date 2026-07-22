class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        
        zero_count=0
        zero=nums.count(0)
        #print(zero)
        n=len(nums)
        #print(n)
        ln=0

        for i in range(len(nums)):
            if nums[i]==0:
                zero_count+=1
            
              
            while zero_count>k:
                if nums[l]==0:
                    zero_count-=1
                l+=1
            ln=max(ln,i-l+1)
        return ln        
