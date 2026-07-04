class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        count=0
        #def LCM(nums):
            
        def lcm(a,b):
            return (a*b) //math.gcd(a,b)
            #return reduce(lcm,nums)    
        for i in range(len(nums)):
            curr_lcm=nums[i]
            for j in range(i,len(nums)):
                curr_lcm=lcm(curr_lcm,nums[j]) #//math.gcd(lcm,nums[j])
                if curr_lcm>k:
                    break
                if curr_lcm==k:
                        
                #sub=nums[i:j+1]
                #if LCM(sub)==k:
                    count+=1
        return count            