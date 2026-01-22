class Solution:
    def search(self, nums: List[int], target: int) -> int:
        arr=nums
        t=target 

        l=0
        h=len(arr)-1
        while (l<=h):
            mid=(l+h)//2
            if arr[mid]==t:
                return mid
            if arr[l]<=arr[mid]:
                if arr[l]<=t and t<arr[mid]:
                    h=mid-1
                else:
                    l=mid+1
            else:


                if arr[mid]< t and arr[h]>=t:
                    l=mid+1
                else:
                    h=mid-1
        return -1



                  