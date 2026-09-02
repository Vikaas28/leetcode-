class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        # res=[]
        # for i in range(len(nums)):
        #     summ=0
        #     for j in range(len(nums)):
        #         if j !=i :
        #             # summ+=max(nums[i],nums[j])-min(nums[i],nums[j])
        #             summ+=abs(nums[i]-nums[j])
        #     res.append(summ)


        # return res
        
        prefix_sum = [0]*len(nums)
        prefix_sum[0]=nums[0]
        for i in range(1,len(nums)):
            prefix_sum[i]=prefix_sum[i-1]+nums[i]
        arr = []
        for i in range(len(nums)):
            left = ((nums[i]*(i+1) )-prefix_sum[i])
            right = (nums[i]*(len(nums) - (i+1))) - (prefix_sum[-1] - prefix_sum[i])
            term = abs(left) + abs(right) 
            arr.append(term)
        return arr         
        