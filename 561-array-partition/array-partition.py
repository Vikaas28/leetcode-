class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        total=0
        for i in range(0,n,2):
            total+=nums[i]
        return total    