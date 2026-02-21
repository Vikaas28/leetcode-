class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l=0
        h=len(nums)-1
        t=target
        while(l<=h):
            mid=(l+h)//2
            
            if nums[mid]==t:
                return True 

            elif nums[l]==nums[mid]==nums[h]:
                l+=1
                h-=1

            elif nums[l]<=nums[mid]:
                if nums[l] <=t and nums[mid]>t:
                    h=mid-1
                else:
                    l=mid+1
            elif nums[mid]<t and nums[h]>=t:
                l=mid+1
            else:
                h=mid-1
        return False


