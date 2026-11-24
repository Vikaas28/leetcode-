
import math
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        l=0
        count=0
        #prod=1

        for i in range(len(nums)):
            prod=1
            for j in range(i,len(nums)):
                prod*=nums[j]
                sub=nums[i:j+1]
                lenn=j-i+1
                lcm=math.lcm(*sub)
                gcd=math.gcd(*sub)
                if prod==lcm*gcd:
                    l=max(l,lenn)
        return l            
                    


        