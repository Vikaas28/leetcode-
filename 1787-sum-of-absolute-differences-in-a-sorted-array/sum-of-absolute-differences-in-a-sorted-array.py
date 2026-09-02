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
        prefix=0
        
        n=len(nums)
        res=[]
        summ=sum(nums)
        for i in range(len(nums)):
            
            leftsum=prefix
            rightsum=summ-prefix-nums[i]
            val=(nums[i]*i-leftsum) +(rightsum-(nums[i]*(n-i-1)))
            res.append(val)
            prefix+=nums[i]
        return res     
            