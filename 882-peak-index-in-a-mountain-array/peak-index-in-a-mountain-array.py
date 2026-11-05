class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        l=0
        h=len(arr)-1
        while l < h:
            mid=(l+h)//2
            if arr[mid]>arr[mid+1]:
                h=mid
            else:
                l=mid+1
        return l            