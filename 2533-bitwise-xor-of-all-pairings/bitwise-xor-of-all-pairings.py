class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        n=len(nums1)
        ans=0
        #minn=float('inf')
        m=len(nums2)
        if n%2!=0:
            for i in nums2:
                ans^=i
        if m%2!=0:
            for i in nums1:
                ans^=i
        return ans                 