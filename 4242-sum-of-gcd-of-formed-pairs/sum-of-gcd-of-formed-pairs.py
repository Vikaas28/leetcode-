class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n=len(nums)
        prefix=[0]*n
        l=0
        r=n-1
        mxx=nums[0]
        for i  in range(n):
            mxx=max(mxx,nums[i])
            prefix[i]=math.gcd(nums[i],mxx)
            # prefixGcd[i] = gcd(nums[i], mxi)
           
        prefix.sort()
        summ=0
        while l<r :
            summ+=math.gcd(prefix[l],prefix[r]) 
            l+=1
            r-=1    
        return summ     



        
           



