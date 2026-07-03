class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left =0
        
        window_sum=0
        max_freq=0
        for i in range(len(nums)):
            window_sum+=nums[i]
            print(window_sum,i-left+1)
           
            #total number of element in window is w-len= i -left +1
            #total sum if all elements are equal is len(nums)*num[i]
            #operation to perform (w_len*nums[i])-window_sum
            #op=(w_len*nums[i])-window_sum
            while ((i-left+1)*nums[i])-window_sum >k:
                window_sum-=nums[left]
                left+=1
            w_len=i-left+1    
            max_freq=max(max_freq,w_len)
        return max_freq        
        

