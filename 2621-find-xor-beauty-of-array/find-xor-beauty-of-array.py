class Solution:
    def xorBeauty(self, nums: list[int]) -> int:
        ans=0
        for i in nums:
            ans^=i
        return ans    