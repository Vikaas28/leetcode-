class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(n):
            ans=0
            while n >0:

                #temp=n
                ans=ans*10 +(n%10)
                n//=10

            return ans
        
        # count =0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + rev(nums[j])==nums[j]+rev(nums[i]):
        #             count+=1
        # return count
        
        #freq=Counter(nums)
        freq={}
        count =0
        mod=10**9 +7 
        for i in range(len(nums)):
            diff = nums[i]-rev(nums[i])
            count+=freq.get(diff,0)
            freq[diff]=freq.get(diff,0)+1
            
            
        return count % mod     
            
        