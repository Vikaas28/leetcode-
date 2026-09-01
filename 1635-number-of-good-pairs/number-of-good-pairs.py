class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # count=0
        # for i in range(len(nums)):
        #     #count=0
        #     for j in range(1,len(nums)):
        #         if i < j and nums[i]==nums[j]:
        #             count+=1
        # return count  

        freq=Counter(nums)
        return sum(count*(count-1)//2 for count in freq.values())
                      
        