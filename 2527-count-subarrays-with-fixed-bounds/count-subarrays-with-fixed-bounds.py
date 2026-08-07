class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # def most(minK, maxK):
        #     l=0
        #     count=0
        #     for i  in range(len(nums)):
        #         maxx=nums[0]
        #         minn=nums[0]
  
        #         while maxx !=maxK and minn !=minK:
        #             i-=1
                
        #             l+=1
        #         count+=i-l+1
        #     return count   
        # return most(minK,maxK)-most(minK,maxK-1)         
        ans=0
        bad=-1
        last=-1
        first=-1
        for i, num in enumerate(nums):
            if num < minK or  num>maxK:
                bad=i
            if num ==maxK:
                last=i
            if num==minK:
                first=i        
            a=min(last, first )-bad
            if a>0:
                ans+=a

        return ans      
        