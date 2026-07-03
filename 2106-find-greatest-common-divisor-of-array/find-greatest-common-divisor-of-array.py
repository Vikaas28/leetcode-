class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(nums):
            if not nums:
                return 
            small=min(nums)

            large=max(nums)
            return math.gcd(small,large)    
            
        return gcd(nums)        