class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count=0
        for i in range(n):
            gcd=0
            for j in range(i, n):
                #sub=nums[i:j+1]
                gcd=math.gcd(gcd,nums[j])
                if gcd<k:
                    break
                if gcd==k:
                    count+=1    
                #if reduce(math.gcd,sub)==k:
                       
        return count        