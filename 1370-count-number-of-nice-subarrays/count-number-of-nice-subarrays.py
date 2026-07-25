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
        
        #Optimal approah two pointer variable lenght 
        def atMost(k):
            if k<0:
                return 0
            l=0
            count=0
            odd_count=0
            summ=0
            for r in range(len(nums)):
                if nums[r]%2!=0:
                    odd_count+=1
                while odd_count>k:
                    if nums[l]%2!=0:

                        odd_count-=1
                    l+=1
                count+=(r-l+1)
            return count      
        return atMost(k)-atMost(k-1)

