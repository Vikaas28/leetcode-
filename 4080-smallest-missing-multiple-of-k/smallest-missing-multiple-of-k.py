class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # seen=set(nums)
        # mul=k
        # while mul in seen:
        #     mul+=k
        # return mul 
        freq={}
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
        mul=k
        while mul in freq:
            mul+=k
        return mul            