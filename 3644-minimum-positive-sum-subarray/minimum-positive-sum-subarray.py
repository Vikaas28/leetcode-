class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        minn=float('inf')
        
        count=0
        #summ=0
        for i in range(len(nums)):
            summ=0
            for j in range(i,min(len(nums),i+r)):
                summ+=nums[j]
                
                if j-i+1>=l and summ>0:
                    minn=min(minn,summ)
        return minn if minn !=float('inf') else -1            


        