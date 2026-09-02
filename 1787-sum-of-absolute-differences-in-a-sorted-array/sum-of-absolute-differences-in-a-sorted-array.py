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
        n=len(nums)
        for i in range(1,len(nums)):
            prefix_sum[i]=prefix_sum[i-1]+nums[i]
        arr = []
        for i in range(len(nums)):
            left_sum = prefix_sum[i - 1] if i > 0 else 0
            left = (nums[i] * i) - left_sum
            
            # Elements strictly to the right: (n - i - 1) elements, sum is total - prefix_sum[i]
            right_sum = prefix_sum[-1] - prefix_sum[i]
            right = right_sum - (nums[i] * (n - i - 1))

            term = abs(left) + abs(right) 
            arr.append(term)
        return arr         
        