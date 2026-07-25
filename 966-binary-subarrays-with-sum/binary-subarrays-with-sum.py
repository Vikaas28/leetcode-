class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # summ =0
        # count=0
        # l=0

        # for r in range(len(nums)):
        #     summ+=nums[r]
        #     while summ>goal:
        #         count+=1
        # return count         
        #pattern 3 count --> prefix + hasp map
        prefix=0
        mp={0:1}
        count=0
        for x in nums:
            prefix+=x
            if prefix-goal in mp:
                count +=mp[prefix-goal]
            mp[prefix]=mp.get(prefix,0)+1
        return count         