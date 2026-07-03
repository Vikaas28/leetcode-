
import math
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        def GCD(nums):
            if not nums:
                return 0
            return reduce(math.gcd,nums)
        def LCM(nums):
            if not nums:
                return 0
            def lcm(a, b):
                return (a*b)//math.gcd(a,b)        
            return reduce(lcm,nums)
        ans=GCD(nums) *LCM(nums)
        for i  in range(len(nums)):
            remain=nums[:i] + nums[i+1:] 
            gcd=GCD(remain)
            lcm=LCM(remain)
            ans=max(ans,gcd*lcm)
        return ans         