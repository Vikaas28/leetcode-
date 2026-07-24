class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans =0 
        ws=sum(nums[:k])
        max_avg=ws/k
        for i in range(k,len(nums)):
            ws+=nums[i]
            ws-=nums[i-k]
            avg=ws/k

            max_avg=max(max_avg,avg)

        return max_avg