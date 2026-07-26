class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count =0
        l=0
        curr=1

        for i in range(len(nums)):
            curr*=nums[i]
            while curr>=k and l<=i:
                

                    curr//=nums[l]
                    l+=1
            count+=(i-l+1) 
        return count         