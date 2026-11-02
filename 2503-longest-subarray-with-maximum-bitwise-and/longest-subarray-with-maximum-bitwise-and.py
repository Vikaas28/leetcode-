class Solution:
    def longestSubarray(self, nums: list[int]) -> int:

        ln=0
        end=0
        l=0
        maxx=max(nums)
        for i in range(len(nums)):
            if nums[i]==maxx:
                end+=1
                ln=max(ln,end)
            else:
                end=0
        return ln             