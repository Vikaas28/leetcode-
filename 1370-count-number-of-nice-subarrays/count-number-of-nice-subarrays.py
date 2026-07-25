class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        #BRUTE FORCE Approach 
        # count=0
        # #odd_count=0
        # for i in range(len(nums)):
        #     odd_count=0
        #     for j in range(i,len(nums)):
        #         if nums[j]%2!=0:
        #             odd_count+=1
        #         if odd_count==k:
        #             count+=1
        #         elif odd_count>k :
        #             break

        # return count    
        
        #Optimal approah count  hash map + prefix
        mp={0:1}
        prefix=0
        odd_count=0
        ans=0
        for i in range(len(nums)):
            prefix+=nums[i]
            if nums[i]%2!=0:
                odd_count +=1
            if odd_count -k in mp:
                ans+=mp.get(odd_count-k,0)
            mp[odd_count]=mp.get(odd_count,0)+1
        return ans         