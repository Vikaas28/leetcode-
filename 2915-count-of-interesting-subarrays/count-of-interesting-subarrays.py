class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count=0
        prefix=0
        mp={0:1}
        for i in range(len(nums)):
            if nums[i]%modulo ==k:
                nums[i]=1
            else:
                nums[i]=0
        for j in range(len(nums)):        
            prefix+=nums[j]
            curr=prefix%modulo
            # r1=s1%m  r2 =s2 %m 
            # (s1 -s2)%m ==k
            # r1=curr
            r2=(curr-k+modulo)%modulo

            if r2 in mp:
                count+=mp.get(r2,0) 
            mp[curr]=mp.get(curr,0)+1
        return count           
        #print(nums)            
